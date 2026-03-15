class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"\nYou borrowed '{book.get_title()}'.")
        else:
            print("\nThat book is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"\nYou returned '{book.get_title()}'.")
        else:
            print("\nYou did not borrow that book.")
