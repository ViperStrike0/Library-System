from book import Book, FictionBook, NonFictionBook, ReferenceBook
from prettytable import PrettyTable
from library_utils import books_to_prettytable


class Library():
    def __init__(self) -> None:
        self.books_list = []
        self.members_list = []

    def show_book_details(self):
        print("\n***   These book are found in the Library   ***")
        print(books_to_prettytable(self.books_list))

    def update_book_quantity(self, isbn):
        for row in self.myTable._rows:
            if row[3] == isbn:
                if row[4] == 0:
                    print("there is no enough books!")
                    return
                else:
                    row[4] -= 1
                    break
        print("Book Quantity updated successfully")

    def show_book_availability(self):
        pass

    def add_book(self, book):
        self.books_list.append(book)
        print(f"*** book added successfully! ***")

    def add_member(self, library_member):
        self.members_list.append(library_member)
        print("member added successfully\n")

    def find_member_by_id(self, member_id):
        for member in self.members_list:
            if member.member_id == member_id:
                return member
        print("Member not found.")
        return None

    def check_member_booked_books(self):
        member_id = input("member id: ")
        member = self.find_member_by_id(member_id)

        if member:
            member.show_borrowed_books()
        else:
            print("member not found!")

    def find_book_by_isbn(self, isbn):
        for book in self.books_list:
            if book.isbn == isbn:
                return book
        print("Book not found.")
        return False

    def borrow_book_for_member(self):
        print(books_to_prettytable(self.books_list))
        member_id = input("Member ID : ")
        search_book_isbn = input("Book ISBN : ")

        book = self.find_book_by_isbn(search_book_isbn)
        member = self.find_member_by_id(member_id)

        if member:
            if book:
                # self.update_book_quantity(book.isbn)
                for book in self.books_list:
                    if book.isbn == search_book_isbn:
                        member.borrow_book(book)
