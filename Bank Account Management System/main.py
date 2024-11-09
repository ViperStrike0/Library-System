from book import Book, FictionBook, NonFictionBook, ReferenceBook
from libraryMember import LibraryMember, Student, Teacher
from library import Library

library = Library()


def main_menu():
    while True:
        print("\n   ***  Welcome to book my Library!  ***   ")
        print("1. Books Management")
        print("2. Members Management")
        print("0. exit")
        choice = input("Enter your Choice: ")
        if choice == "1":
            while True:
                print("***   Books Menu   ***")
                print("1. add book to the library")
                print("2. display book in the library")
                print("0. return to main menu")
                choice = input(">> ")
                if choice == "1":
                    title = input("enter book's title : ")
                    author = input("enter book's author : ")
                    isbn = input("enter book's isbn : ")
                    quantity = input("Enter book's quantity : ")
                    print("1. Fiction")
                    print("2. Non-Fiction")
                    print("3. Reference")
                    book_type = input("Enter choice (1/2/3): ")
                    if book_type == "1":
                        book = FictionBook(title, author, isbn, quantity)
                    elif book_type == "2":
                        book = NonFictionBook(title, author, isbn, quantity)
                    elif book_type == "3":
                        book = ReferenceBook(title, author, isbn, quantity)
                    else:
                        print("Invaild book type!")
                        return

                    library.add_book(book)

                elif choice == "2":
                    library.show_book_details()
                elif choice == "0":
                    break
                else:
                    print("Ener Valid Number!")

        elif choice == "2":
            while True:
                print("***   Members Management   ***")
                print("1. add a new Member")
                print("2. show all booked books")
                print("3. borrow a book")
                print("4. return a book")
                print("0. return to main menu")
                choice = input(">> ")
                if choice == "1":
                    member_name = input("member's name : ")
                    member_id = input("member_id")
                    member_type = input(
                        "select member type:\n1.student \n2.teacher")
                    if member_type == "1":
                        new_member = Student(member_name, member_id)
                    elif member_type == "2":
                        new_member = Teacher(member_name, member_id)
                    else:
                        print("Please enter a valid member type!")
                        continue
                    library.add_member(new_member)

                elif choice == "2":
                    library.check_member_booked_books()

                elif choice == "3":
                    library.borrow_book_for_member()

                elif choice == "0":
                    break
                else:
                    print("Enter Valid Number!")
                    continue

        elif choice == "0":
            break

        else:
            print("Enter valid number")
            continue


main_menu()
