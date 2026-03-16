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

try:
    user_name = input("What is your name? ").strip()
except KeyboardInterrupt:
    print("\n\nProgram stopped.")
    raise SystemExit(0)

if not user_name:
    user_name = "Guest"

user = User(user_name)

print(f"\nWelcome, {user.name}.")

try:
    while True:
        print("\n=== Library Menu ===")
        print("1. Show books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            clear_screen()
            library.show_books()

        elif choice == "2":
            clear_screen()
            library.show_books()

            try:
                index = int(input("\nEnter the book number to borrow: ")) - 1

                if index < 0 or index >= len(library.books):
                    print("\nThat is not a valid book number.")
                else:
                    user.borrow_book(library.books[index])
                    library.show_books()

            except ValueError:
                print("\nPlease enter numbers only.")

        elif choice == "3":
            clear_screen()
            library.show_books()

            try:
                index = int(input("\nEnter the book number to return: ")) - 1

                if index < 0 or index >= len(library.books):
                    print("\nThat is not a valid book number.")
                else:
                    user.return_book(library.books[index])
                    library.show_books()

            except ValueError:
                print("\nPlease enter numbers only.")

        elif choice == "4":
            clear_screen()
            print("\nThanks for using the library.")
            break

        else:
            print("\nInvalid option. Please choose a number between 1 and 4.")
except KeyboardInterrupt:
    print("\n\nProgram stopped.")
