class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._available = True

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def is_available(self):
        return self._available

    def borrow(self):
        if self._available:
            self._available = False
            return True
        return False

    def return_book(self):
        self._available = True