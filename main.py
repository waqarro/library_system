import os
from models.book import Book
from models.user import User
from services.library import Library


library = Library()

book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("48 law of power", "Robert Greene")
book3 = Book("The Alchemist", "Paulo Coelho")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("\nWelcome to the Library!")
print("-" * 50)

user_name = input("Enter your name: ")
user = User(user_name)

print(f"\nWelcome, {user.name}!")

while True:
    print("\n=== Library Menu ===")
    print("1. Show books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        os.system('cls')    #this is for window to clean the terminal
        os.system('clear')  #and this one is for mac and linux to clean the terminal 
        
        library.show_books()

    elif choice == "2":
        os.system('cls')   
        os.system('clear') 
        library.show_books()

        try:
            index = int(input("\nEnter the book number to borrow: ")) - 1

            if index < 0 or index >= len(library.books):
                print("\nInvalid book number.")
            else:
                user.borrow_book(library.books[index])

        except ValueError:
            print("\nPlease enter a valid number.")

    elif choice == "3":
        os.system('cls')   
        os.system('clear') 
        library.show_books()

        try:
            index = int(input("\nEnter the book number to return: ")) - 1

            if index < 0 or index >= len(library.books):
                print("\nInvalid book number.")
            else:
                user.return_book(library.books[index])

        except ValueError:
            print("\nPlease enter a valid number.")

    elif choice == "4":
        os.system('cls')  
        os.system('clear')
        print("\nThank you, and have a nice day.")
        break

    else:
        print("\nInvalid option. please choose between 1 and 4.")
