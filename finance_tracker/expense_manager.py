from finance_tracker.expense import Expense
from finance_tracker.file_handler import load_expenses, save_expenses

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD): ")

    expense = Expense(amount, category, description, date)
    expenses = load_expenses()
    expenses.append(expense.to_dict())
    save_expenses(expenses)

    print("\nExpense added successfully!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n--- ALL EXPENSES ---")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. ₹{e['amount']} | {e['category']} | {e['description']} | {e['date']}")

def search_expenses():
    keyword = input("Enter category to search: ").lower()
    expenses = load_expenses()

    print("\n--- SEARCH RESULTS ---")
    for e in expenses:
        if keyword in e["category"].lower():
            print(f"₹{e['amount']} | {e['category']} | {e['description']} | {e['date']}")
