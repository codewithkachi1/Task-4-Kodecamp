from budget_utils import load_transactions, save_transactions, group_by_category, calculate_totals
from transaction import Transaction

def main():
    filename = "transactions.json"
    transactions = load_transactions(filename)

    while True:
        print("Personal Budget Tracker")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. Group by category")
        print("4. Calculate totals")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            transaction = Transaction(date, category, amount)
            transactions.append(transaction)
            save_transactions(transactions, filename)
        elif choice == "2":
            for transaction in transactions:
                print(f"Date: {transaction.date.strftime('%Y-%m-%d')}, Category: {transaction.category}, Amount: {transaction.amount}")
        elif choice == "3":
            categories = group_by_category(transactions)
            for category, amount in categories.items():
                print(f"Category: {category}, Total: {amount}")
        elif choice == "4":
            total_income, total_expenses = calculate_totals(transactions)
            print(f"Total Income: {total_income}, Total Expenses: {total_expenses}")
        elif choice == "5":
            break
        else:
            print("Invalid choice")

main()