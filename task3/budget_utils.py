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

