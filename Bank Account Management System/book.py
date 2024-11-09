from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, isbn, quantity) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = int(quantity)
        self._is_available = True 
    def get_type(self):
        return "Unknown"
    def get_description(self):
        pass
    def borrow(self):
        self.quantity -= 1
    def toggle_availability(self):
        self._is_available = True
    def is_available(self):
        return self.quantity > 0

class FictionBook(Book):
    def get_description(self):
        print("This is a FictionBook")
    def get_type(self):
        return "Fiction"  

class NonFictionBook(Book):
    def get_description(self):
        print("This is a NonFictionBook")
    def get_type(self):
        return "NonFiction"
    
class ReferenceBook(Book):
    def get_description(self):
        print("This is a ReferenceBook")
    def get_type(self):
        return "Reference"    
