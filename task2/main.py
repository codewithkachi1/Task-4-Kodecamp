from inventory import Inventory
from book import Book

def main():
    filename = "books.json"
    inventory = Inventory(filename)

    while True:
        print("Bookstore Inventory System")
        print("1. Add book")
        print("2. View books")
        print("3. Search book")
        print("4. Update stock")
        print("5. Update price")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter stock: "))
            book = Book(title, author, price, stock)
            inventory.add_book(book)
        elif choice == "2":
            inventory.view_books()
        elif choice == "3":
            title = input("Enter title: ")
            book = inventory.search_book(title)
            if book:
                print(f"Title: {book.title}, Author: {book.author}, Price: {book.price}, Stock: {book.stock}")
            else:
                print("Book not found")
        elif choice == "4":
            title = input("Enter title: ")
            stock = int(input("Enter new stock: "))
            inventory.update_stock(title, stock)
        elif choice == "5":
            title = input("Enter title: ")
            price = float(input("Enter new price: "))
            inventory.update_price(title, price)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

main()


# Git Commands:

# 1. Create a new branch for the search feature: git checkout -b feature-search
# 2. Implement the search feature in the inventory.py file
# 3. Commit the changes: git add . and `git commit -m "Added search feature, searching by title")
# 4. Switch back to the main branch: git checkout main
# 5. Merge the feature branch: git merge feature-search
# 6. Push the changes to the remote repository: git push origin main