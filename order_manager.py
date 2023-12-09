class OrderManager:
    def __init__(self):
        self.orders = []

    def process_order(self, order):
        # Add logic to process orders
        order.status = "Processed"
        self.notify_customer(order)

    def notify_customer(self, order):
        # Add logic to notify customers about order status
        print(f"Notification sent to {order.customer} for Order ID {order.order_id}: Order {order.status}")

    def display_order_details(self):
        # Add logic to display order details
        for order in self.orders:
            print(f"Order ID: {order.order_id}, Items: {order.items}, Customer: {order.customer}, Status: {order.status}")

class Order:
    def __init__(self, order_id, items, customer):
        self.order_id = order_id
        self.items = items
        self.customer = customer
        self.status = "Pending"

# Sweet Delight Bakery System:

# Creating an OrderManager instance
order_manager = OrderManager()

# Creating an Order instance
order1 = Order(order_id=1, items=["Item1", "Item2"], customer="John Smith")
order2 = Order(order_id=2, items=["Item2", "Item3"], customer="Sarah Bond")
order3 = Order(order_id=3, items=["Item4", "Item5"], customer="Holly Pathaway")
order4 = Order(order_id=4, items=["Item3", "Item2"], customer="Daniel Do")
order5 = Order(order_id=5, items=["Item1", "Item4"], customer="David Brown")

# Adding the order to the OrderManager's orders list
order_manager.orders.extend([order1, order2, order3, order4, order5])

# Processing the order
for order in order_manager.orders:
    order_manager.process_order(order)

# Displaying order details after processing
order_manager.display_order_details()
