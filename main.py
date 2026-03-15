from models.book import Book
from models.user import User
from services.library import Library

library = Library()

# create books
book1 = Book("Python Basics", "John Smith")
book2 = Book("AI Fundamentals", "Alice Brown")

library.add_book(book1)
library.add_book(book2)

# create user
user = User("Waqar")

while True:
    print("\nLibrary Menu")
    print("1. Show Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        library.show_books()

    elif choice == "2":
        library.show_books()
        index = int(input("Enter book number: ")) - 1
        user.borrow_book(library.books[index])

    elif choice == "3":
        library.show_books()
        index = int(input("Enter book number: ")) - 1
        user.return_book(library.books[index])

    elif choice == "4":
        break