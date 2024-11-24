import sqlite3
import secrets
import string

DATABASE = 'users.db'

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

        admin_username = 'admin'
        admin_password = generate_random_password()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (admin_username, admin_password))
        conn.commit()


if __name__ == '__main__':
    init_db()