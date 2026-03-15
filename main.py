import os
from models.book import Book
from models.user import User
from services.library import Library


def clear_screen():
    command = "cls" if os.name == "nt" else "clear"
    if os.name == "nt" or os.getenv("TERM"):
        os.system(command)


library = Library()

book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("The 48 Laws of Power", "Robert Greene")
book3 = Book("The Alchemist", "Paulo Coelho")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

user_name = input("Enter your name: ")
user = User(user_name)

print(f"\nWelcome to the library, {user.name}.")

while True:
    print("\n=== Library Menu ===")
    print("1. Show books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        clear_screen()
        library.show_books()

    elif choice == "2":
        clear_screen()
        library.show_books()

        try:
            index = int(input("\nEnter the book number to borrow: ")) - 1

            if index < 0 or index >= len(library.books):
                print("\nThat book number is not valid.")
            else:
                user.borrow_book(library.books[index])

        except ValueError:
            print("\nPlease enter a number only.")

    elif choice == "3":
        clear_screen()
        library.show_books()

        try:
            index = int(input("\nEnter the book number to return: ")) - 1

            if index < 0 or index >= len(library.books):
                print("\nThat book number is not valid.")
            else:
                user.return_book(library.books[index])

        except ValueError:
            print("\nPlease enter a number only.")

    elif choice == "4":
        clear_screen()
        print("\nThanks for using the library system.")
        break

    else:
        print("\nInvalid option. Please choose a number from 1 to 4.")
