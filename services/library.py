from tabulate import tabulate
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
             if not self.books:
                print("\nNo books are currently available.")
             return
     
    table = []
     
    for i, book in enumerate(self.books):
             status = "Available" if book.is_available() else "Borrowed"
             table.append([i + 1, book.get_title(), book.get_author(), status])
     
             print("\nAvailable Books")
             print(tabulate(table, headers=["No", "Title", "Author", "Status"], tablefmt="grid"))
     
             print("\nAvailable Books")
             print("-" * 50)
         
    for i, book in enumerate(self.books):
            status = "Available" if book.is_available() else "Borrowed"
            print(f"{i + 1}. {book.get_title()} by {book.get_author()} ({status})")
