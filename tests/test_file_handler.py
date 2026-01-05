import unittest
import os
import json
from finance_tracker.file_handler import load_expenses, save_expenses

TEST_FILE = "data/expenses.json"

class TestFileHandler(unittest.TestCase):

    def setUp(self):
        # Create test data before each test
        self.test_data = [
            {
                "amount": 100,
                "category": "Food",
                "description": "Snacks",
                "date": "2026-01-01"
            }
        ]
        save_expenses(self.test_data)

    def test_load_expenses(self):
        expenses = load_expenses()
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["category"], "Food")

    def test_save_expenses(self):
        expenses = load_expenses()
        self.assertIsInstance(expenses, list)

    def tearDown(self):
        # Clean up after test
        with open(TEST_FILE, "w") as file:
            json.dump([], file)


if __name__ == "__main__":
    unittest.main()
