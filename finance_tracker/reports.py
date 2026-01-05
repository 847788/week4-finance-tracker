from finance_tracker.file_handler import load_expenses

def monthly_report():
    month = input("Enter month (YYYY-MM): ")
    expenses = load_expenses()
    total = 0

    for e in expenses:
        if e["date"].startswith(month):
            total += e["amount"]

    print(f"\nTotal expenses for {month}: ₹{total}")

def category_breakdown():
    expenses = load_expenses()
    categories = {}

    for e in expenses:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]

    print("\n--- CATEGORY BREAKDOWN ---")
    for cat, amt in categories.items():
        print(f"{cat}: ₹{amt}")
