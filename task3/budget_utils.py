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

