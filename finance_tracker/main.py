from finance_tracker.utils import show_header, show_menu
from finance_tracker.expense_manager import add_expense, view_expenses, search_expenses
from finance_tracker.reports import monthly_report, category_breakdown
from finance_tracker.file_handler import backup_data

def main():
    show_header()

    while True:
        show_menu()
        choice = input("Enter your choice (0-9): ")

        if choice == "1":
            print("\n--- ADD NEW EXPENSE ---")
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            monthly_report()
        elif choice == "5":
            category_breakdown()
        elif choice == "9":
            backup_data()
            print("\nBackup completed!")
        elif choice == "0":
            print("\nThank you for using Personal Finance Tracker!")
            break
        else:
            print("\nInvalid choice! Please try again.")
