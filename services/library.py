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

        for index, book in enumerate(self.books, start=1):
            status = "Available" if book.is_available() else "Borrowed"
            borrowed_at = "-"

            if book.get_borrow_time():
                borrowed_at = book.get_borrow_time().strftime("%d/%m/%Y %I:%M %p")

            table.append(
                [index, book.get_title(), book.get_author(), status, borrowed_at]
            )

        print("\nAvailable Books")
        print(
            tabulate(
                table,
                headers=["No.", "Title", "Author", "Status", "Borrowed At"],
                tablefmt="grid",
            )
        )
