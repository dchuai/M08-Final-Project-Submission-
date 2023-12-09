from .user_manager import UserManager
from .inventory_manager import InventoryManager
from .order_manager import OrderManager

class SweetDelightsBakery:
    def __init__(self):
        self.user_manager = UserManager()
        self.inventory_manager = InventoryManager()
        self.order_manager = OrderManager()

    def start(self):
        # Add initialization logic or start the graphical user interface
        print("Welcome to Sweet Delights Bakery System!")

        # Example: Authenticate user
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if self.user_manager.authenticate(username, password):
            print("Authentication successful!")
            # Add logic for user interaction
        else:
            print("Authentication failed. Please check your credentials.")
