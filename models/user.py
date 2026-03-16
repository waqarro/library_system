class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            borrow_time = book.get_borrow_time().strftime("%d/%m/%Y %I:%M %p")
            print(f"\nYou borrowed \"{book.get_title()}\" at {borrow_time}.")
        else:
            print("\nSorry, that book is not available right now.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"\nYou returned \"{book.get_title()}\".")
        else:
            print("\nYou have not borrowed that book.")
