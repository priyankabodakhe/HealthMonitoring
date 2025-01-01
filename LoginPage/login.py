import sqlite3

class Login:
    def __init__(self):
        self.conn = sqlite3.connect('health_system.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
                         (username TEXT PRIMARY KEY, password TEXT)''')

    def register(self):
        """Handles user registration"""
        print("User Registration")
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            self.c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            print("Registration successful!")
        except sqlite3.IntegrityError:
            print("Username already exists.")
            return False  # Indicate registration failure

        return True  # Indicate registration success

    def log(self):
        """Handles user login"""
        print("User Login")
        username = input("Enter username: ")
        password = input("Enter password: ")

        self.c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = self.c.fetchone()

        if user:
            print(f"Welcome, {username}!")
            return True  # Indicate successful login
        else:
            print("Invalid username or password.")
            return False  # Indicate login failure
