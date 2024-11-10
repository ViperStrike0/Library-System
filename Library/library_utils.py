from prettytable import PrettyTable

def books_to_prettytable(books):
    myTable = PrettyTable(["title", "author","type", "isbn", "quantity"])
    for book in books:
        myTable.add_row([book.title, book.author, book.get_type(),book.isbn,book.quantity])
    return myTable

def borrowed_books_to_prettytable(books):
    myTable = PrettyTable(["title", "author","type"])
    for book in books:
        myTable.add_row([book.title, book.author, book.get_type()])
    return myTable