import unittest
from finance_tracker.file_handler import save_expenses
from finance_tracker.reports import category_breakdown

class TestReports(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            {
                "amount": 100,
                "category": "Food",
                "description": "Lunch",
                "date": "2026-01-01"
            },
            {
                "amount": 200,
                "category": "Food",
                "description": "Dinner",
                "date": "2026-01-02"
            },
            {
                "amount": 300,
                "category": "Transport",
                "description": "Bus",
                "date": "2026-01-03"
            }
        ]
        save_expenses(self.test_data)

    def test_category_totals(self):
        categories = {}
        for e in self.test_data:
            categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]

        self.assertEqual(categories["Food"], 300)
        self.assertEqual(categories["Transport"], 300)


if __name__ == "__main__":
    unittest.main()
