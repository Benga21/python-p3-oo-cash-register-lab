import unittest
import os

from lib.cash_register import CashRegister


class TestCashRegister(unittest.TestCase):
    def test_add_item(self):
        register = CashRegister()
        register.add_item("apple", 1.00, 3)
        self.assertEqual(register.total, 3.00)
        self.assertEqual(register.items, ["apple", "apple", "apple"])

    def test_apply_discount(self):
        register = CashRegister(20)
        register.add_item("banana", 5.00)
        register.apply_discount()
        self.assertEqual(register.total, 4.00)  # 20% off 5.00 is 4.00

    def test_void_last_transaction(self):
        register = CashRegister()
        register.add_item("apple", 1.00, 3)
        register.add_item("banana", 2.00)
        register.void_last_transaction()
        self.assertEqual(register.total, 3.00)  # Removes last transaction (banana)

# To run the tests directly from this script
if __name__ == '__main__':
    unittest.main()
