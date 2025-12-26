import bcrypt
import json
import time

with open("users.json", "r") as file:
    users = json.load(file)

common_passwords = [
    "123456",
    "password",
    "qwerty",
    "letmein",
    "admin"
]

for username, stored_hash in users.items():
    print(f"\nAttempting attack on user: {username}")
    for pwd in common_passwords:
        start = time.time()
        if bcrypt.checkpw(pwd.encode(), stored_hash.encode()):
            print(f"[!] Password cracked: {pwd}")
            break
        else:
            elapsed = time.time() - start
            print(f"Attempt {pwd} failed ({elapsed:.2f}s)")
