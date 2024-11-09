from abc import ABC, abstractmethod
from library_utils import books_to_prettytable

class Notifiable(ABC):
    def notify(self):
        raise NotImplemented("implement in subclass")

class LibraryMember(ABC):
    def __init__(self, name, member_id) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) < self.limit:
            if book.is_available():
                self.borrowed_books.append(book)
    def return_book(self):
        pass

    def remove_borrowed_book(self):
        pass
    
    def show_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"***   {self.name}'s borrowed these Book :   ***")
            print(books_to_prettytable(self.borrowed_books))

        

class Student(LibraryMember, Notifiable):
    def __init__(self, name, member_id) -> None:
        super().__init__(name, member_id)
        self.limit = 3

    def notify(self):
        print("hello Student")


class Teacher(LibraryMember,  Notifiable):
    def __init__(self, name, member_id) -> None:
        super().__init__(name, member_id)
        self.limit = 5
    def notify(self):
        print("hello Teacher")