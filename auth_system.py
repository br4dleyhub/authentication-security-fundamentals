import json
import os
import logging

USERS_FILE = "users.json"

logging.basicConfig(
    filename="logs/auth.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as file:
        return json.load(file)

def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

def register_user():
    users = load_users()
    username = input("Username: ")
    password = input("Password: ")

    if username in users:
        print("User already exists")
        return

    users[username] = password
    save_users(users)

    logging.info(f"User registered: {username}")
    print("User registered successfully")

def login_user():
    users = load_users()
    username = input("Username: ")
    password = input("Password: ")

    if users.get(username) == password:
        logging.info(f"Successful login: {username}")
        print("Login successful")
    else:
        logging.warning(f"Failed login attempt: {username}")
        print("Invalid credentials")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
