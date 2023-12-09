# user_manager.py
class UserManager:
    """Manages user authentication and user-related operations."""

    def __init__(self):
        self.users = {}

    def authenticate(self, username, password):
        """Authenticate user credentials."""
        if username in self.users and self.users[username].password == password:
            return True
        return False

    def create_user(self, username, password):
        """Create a new user."""
        if username not in self.users:
            self.users[username] = User(username, password)
            print(f"User {username} created successfully.")
        else:
            print(f"User {username} already exists.")

    def get_user(self, username):
        """Get a user by username."""
        return self.users.get(username, None)
