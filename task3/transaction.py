from datetime import datetime

class Transaction:
    def __init__(self, date, category, amount):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.category = category
        self.amount = amount

    def to_dict(self):
        return {
            "date": self.date.strftime("%Y-%m-%d"),
            "category": self.category,
            "amount": self.amount
        }

    @classmethod
    def from_dict(cls, transaction_dict):
        return cls(
            transaction_dict["date"],
            transaction_dict["category"],
            transaction_dict["amount"]
        )