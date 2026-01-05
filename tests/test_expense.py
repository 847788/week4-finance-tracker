import unittest
from finance_tracker.expense import Expense

class TestExpense(unittest.TestCase):

    def test_expense_creation(self):
        expense = Expense(100, "Food", "Lunch", "2026-01-05")

        self.assertEqual(expense.amount, 100)
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.description, "Lunch")
        self.assertEqual(expense.date, "2026-01-05")

    def test_to_dict(self):
        expense = Expense(200, "Transport", "Bus ticket", "2026-01-04")
        expense_dict = expense.to_dict()

        self.assertIsInstance(expense_dict, dict)
        self.assertEqual(expense_dict["amount"], 200)
        self.assertEqual(expense_dict["category"], "Transport")
        self.assertEqual(expense_dict["description"], "Bus ticket")
        self.assertEqual(expense_dict["date"], "2026-01-04")


if __name__ == "__main__":
    unittest.main()
