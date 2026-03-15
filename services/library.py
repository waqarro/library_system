class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def show_books(self):
        if not self.books:
            print("No books in library")
            return

        for i, book in enumerate(self.books):
            status = "Available" if book.is_available() else "Borrowed"
            print(f"{i+1}. {book.get_title()} by {book.get_author()} - {status}")