class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class InventoryManager:
    def __init__(self):
        self.inventory = {}
        self.alerts = []

    def add_item_to_inventory(self, item):
        if item.name not in self.inventory:
            self.inventory[item.name] = item
        else:
            # Update quantity if the item already exists in the inventory
            self.inventory[item.name].quantity += item.quantity

    def update_inventory(self, order_items):
        for item in order_items:
            if item.name in self.inventory:
                # Check if there is enough quantity in the inventory
                if self.inventory[item.name].quantity >= item.quantity:
                    # Fulfill the order by reducing the quantity in the inventory
                    self.inventory[item.name].quantity -= item.quantity
                else:
                    # Generate alert for low stock
                    self.alerts.append(f"Alert: Low stock for {item.name}")
            else:
                # Generate alert for out-of-stock items
                self.alerts.append(f"Alert: Item {item.name} is out of stock")

    def send_alert(self, threshold=0):
        # Add logic to send alerts (for demonstration purposes, print alerts to console)
        for alert in self.alerts:
            print(alert)
            if "Low stock" in alert and self.alerts.count(alert) > threshold:
                print("Sending notification to the manager about low stock!")

# Sweet Delight System Process:
if __name__ == "__main__":
    # Creating inventory items
    item1 = InventoryItem("Cakes", 50, 10.99)
    item2 = InventoryItem("Breads", 30, 5.99)
    item3 = InventoryItem("Bread Rolls", 20, 4.99)
    item4 = InventoryItem("Muffins", 40, 7.99)
    item5 = InventoryItem("Cup Cakes", 75, 2.85)

    # Creating an inventory manager
    manager = InventoryManager()

    # Adding items to the inventory
    manager.add_item_to_inventory(item1)
    manager.add_item_to_inventory(item2)
    manager.add_item_to_inventory(item3)
    manager.add_item_to_inventory(item4)
    manager.add_item_to_inventory(item5)

    # Placing an order
    order_items = [
        InventoryItem("Item1", 20, 10.99),
        InventoryItem("Item2", 10, 5.99),
        InventoryItem("Item3", 5, 4.99),
        InventoryItem("Item4", 35, 7.99),
        InventoryItem("Item5", 35, 2.85)
    ]

    # Updating the inventory based on the order
    manager.update_inventory(order_items)

    # Sending alerts if any
    manager.send_alert(threshold=5)

