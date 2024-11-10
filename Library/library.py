from book import Book, FictionBook, NonFictionBook, ReferenceBook
from prettytable import PrettyTable
from library_utils import books_to_prettytable
from libraryMember import LibraryMember, Student, Teacher

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

    def gather_book_input(self):
        title = input("Enter book's title : ")
        author = input("Enter book's author : ")
        isbn = input("Enter book's isbn : ")
        quantity = input("Enter book's quantity : ")

        book_type = input("1. Fiction \n2. Non-Fiction \n3. Reference \n>> ")
        if book_type == "1":
            return FictionBook(title, author, isbn, quantity)
        elif book_type == "2":
            return NonFictionBook(title, author, isbn, quantity)
        elif book_type == "3":
            return ReferenceBook(title, author, isbn, quantity)
        else:
            print("Invalid book type!")
            return None

    def add_book(self):
        book = self.gather_book_input()
        if book :   
            self.books_list.append(book)
            print(f"*** book added successfully! ***")


    def gather_member_input(self):
        member_name = input("member's name: ")
        member_id = input("member's ID: ")
        member_type = input("select member type:\n1.student:  \n2.teacher: ")
        if member_type == "1":
            return Student(member_name, member_id)
        elif member_type == "2":
            return Teacher(member_name, member_id)
        else:
            print("Please enter a valid member type!")
            return None
        
    def add_member(self):
        new_member = self.gather_member_input()
        if new_member:
            self.members_list.append(new_member)
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

        if member and book:
            for book in self.books_list:
                if book.isbn == search_book_isbn:
                    member.borrow_book(book)
