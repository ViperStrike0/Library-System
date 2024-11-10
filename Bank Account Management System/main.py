from book import Book, FictionBook, NonFictionBook, ReferenceBook
from libraryMember import LibraryMember, Student, Teacher
from library import Library

library = Library()

def display_main_menu():
    while True:
        print("\n   ***  Welcome to book my Library!  ***   ")
        print("1. Books Management")
        print("2. Members Management")
        print("0. exit")
        choice = input(">> ")
        if choice == "1":
            display_book_menu()
        elif choice == "2":
            display_members_management()
        elif choice == "0":
            return
        else:
            print("Enter Valid number!")
            continue
    

def display_book_menu():
    while True:
        print("***   Books Menu   ***")
        print("1. add book to the library")
        print("2. display book in the library")
        print("0. return to main menu")
        choice = input(">> ")
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.show_book_details()
        elif choice == "0":
            return
        else:
            print("Enter Valid number!")
            continue

def display_members_management():
    while True:
        print("***   Members Management   ***")
        print("1. add a new Member")
        print("2. show all booked books")
        print("3. borrow a book")
        print("4. return a book")
        print("0. return to main menu")
        choice = input(">> ")
        if choice == "1":
            library.add_member()
        elif choice == "2":
            library.check_member_booked_books()
        elif choice == "3":
            library.borrow_book_for_member()
        elif choice == "4":
            pass
        elif choice == "0":
            return
        else:
            print("Enter Valid number!")
            continue

display_main_menu()