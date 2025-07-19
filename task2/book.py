class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, book_dict):
        return cls(
            book_dict["title"],
            book_dict["author"],
            book_dict["price"],
            book_dict["stock"]
        )