import sqlite3
from flask import Flask, request, redirect, make_response
import uuid
import time
from cryptography.fernet import Fernet

app = Flask("Super Safe")

with open('secret_key.txt', 'r') as f:
    app.secret_key = f.read().strip()

with open('flag.txt', 'r') as f:
    flag = f.read().strip()

key = Fernet.generate_key()
fernet = Fernet(key)

DATABASE = 'users.db'

def query_db(query, args):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, args)
        rv = cursor.fetchall()
        conn.commit()
        return rv

def generate_cookie(user_id, user_ip, ua, timestamp=None, unique_id=None):
    if timestamp is None:
        timestamp = int(time.time())
    if unique_id is None:
        unique_id = uuid.uuid4()
    cookie_str = f"{timestamp}+++{unique_id}+++{user_id}+++{user_ip}+++{ua}"
    return cookie_str

def encrypt_cookie(cookie_str):
    return fernet.encrypt(cookie_str.encode()).decode()

@app.route('/')
def index():
    return """
    <h1>Welcome</h1>
    <p><a href='/register'>Register</a> | <a href='/login'>Login</a></p>
    """

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        try:
            query_db("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            return "Registration successful! <a href='/login'>Login</a>"
        except sqlite3.IntegrityError:
            return "Username already taken. Please choose another."

    return """
    <form method='POST'>
        <label for='username'>Username:</label>
        <input type='text' id='username' name='username' required>
        <label for='password'>Password:</label>
        <input type='password' id='password' name='password' required>
        <input type='submit' value='Register'>
    </form>
    """

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = query_db("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

        if not user:
            return "Invalid username or password."

        user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        user_agent = request.headers.get('User-Agent')
        cookie_str = generate_cookie(username, user_ip, user_agent)
        encrypted_cookie = encrypt_cookie(cookie_str)

        resp = make_response(redirect('/protected'))
        resp.set_cookie('session', encrypted_cookie, max_age=5)
        return resp

    return """
    <form method='POST'>
        <label for='username'>Username:</label>
        <input type='text' id='username' name='username' required>
        <label for='password'>Password:</label>
        <input type='password' id='password' name='password' required>
        <input type='submit' value='Login'>
    </form>
    """

@app.route('/protected')
def protected():
    cookie = request.cookies.get('session')
    if not cookie:
        return "Access Denied. No session cookie found."
    
    decrypted_cookie = fernet.decrypt(cookie.encode()).decode()
    parts = decrypted_cookie.split('+++', 4)
    if len(parts) < 5:
        return "Access Denied. Invalid session cookie structure."

    timestamp, unique_id, user_id, user_ip, ua = parts[0], parts[1], parts[2], parts[3], parts[4]

    current_user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    current_user_agent = request.headers.get('User-Agent')

    if user_ip != current_user_ip or ua != current_user_agent:
        return f"Access Denied. IP address or User-Agent mismatch."

    current_time = int(time.time())
    if current_time - int(timestamp) > 5:
        return "Access Denied. Cookie expired."

    regenerated_cookie_str = generate_cookie(user_id, user_ip, ua, timestamp=int(timestamp), unique_id=unique_id)

    if regenerated_cookie_str == decrypted_cookie:
        if user_id == 'admin':
            return f"Welcome, {user_id}! Here is your flag: {flag}"
        else:
            return f"Hello, {user_id}! You do not have admin access."
    else:
        return "Access Denied. Cookie integrity check failed."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')