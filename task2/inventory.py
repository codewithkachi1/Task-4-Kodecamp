import json
import math
from book import Book

class Inventory:
    def __init__(self, filename):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Book.from_dict(book_dict) for book_dict in data]
        except FileNotFoundError:
            return []

    def save_books(self):
        data = [book.to_dict() for book in self.books]
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def view_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Price: {book.price}, Stock: {book.stock}")

    

    def update_stock(self, title, stock):
        book = self.search_book(title)
        if book:
            book.stock = stock
            self.save_books()
            print("Stock updated successfully")
        else:
            print("Book not found")

    def update_price(self, title, price):
        book = self.search_book(title)
        if book:
            book.price = math.ceil(price * 100) / 100  # round price to 2 decimal places
            self.save_books()
            print("Price updated successfully")
        else:
            print("Book not found")

# Git Commands:

# 1. Create a new branch for the search feature: git checkout -b feature-search
# 2. Implement the search feature in the inventory.py file
# 3. Commit the changes: git add . and `git commit -m "Added search feature, searching by title")
# 4. Switch back to the main branch: git checkout main
# 5. Merge the feature branch: git merge feature-search
# 6. Push the changes to the remote repository: git push origin main