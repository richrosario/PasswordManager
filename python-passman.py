import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
        # Covers the password being entered
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # Hashes the password
    password_manager[username] = hashed_password
        # Stores as a key value pair in our dictionary
    print("Account created Successfully!")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # Does our key/value pair match our dictionary?
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful")
    else:
        print("Invalid credentials")

def main():
    while True:
        choice = input("1 to create an account\n2 to login\n3 to print passwords\n0 to exit ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print(password_manager)
        elif choice == "0":
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()