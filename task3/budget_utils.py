import json
import os
from transaction import Transaction

def load_transactions(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
            return [Transaction.from_dict(transaction_dict) for transaction_dict in data]
    else:
        return []

def save_transactions(transactions, filename):
    data = [transaction.to_dict() for transaction in transactions]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def group_by_category(transactions):
    categories = {}
    for transaction in transactions:
        if transaction.category in categories:
            categories[transaction.category] += transaction.amount
        else:
            categories[transaction.category] = transaction.amount
    return categories

def calculate_totals(transactions):
    total_income = sum(transaction.amount for transaction in transactions if transaction.amount > 0)
    total_expenses = sum(abs(transaction.amount) for transaction in transactions if transaction.amount < 0)
    return total_income, total_expenses