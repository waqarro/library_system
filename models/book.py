import datetime


class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._available = True
        self.borrow_time = None

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def is_available(self):
        return self._available

    def get_borrow_time(self):
        return self.borrow_time

    def borrow(self):
        if self._available:
            self._available = False
            self.borrow_time = datetime.datetime.now()
            return True
        return False

    def return_book(self):
        self._available = True
        self.borrow_time = None
