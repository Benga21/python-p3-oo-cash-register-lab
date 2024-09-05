class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction = 0

    def add_item(self, item_name, price, quantity=1):
        # Add item price * quantity to total
        self.last_transaction = price * quantity
        self.total += self.last_transaction
        # Add item to the list as many times as its quantity
        self.items.extend([item_name] * quantity)

    def apply_discount(self):
        # Apply discount if available
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Remove the last transaction from the total
        self.total -= self.last_transaction
