from utils import books,issue_books

def return_book():
    book_name = input("Enter book_name:")
    if book_name in issue_books:
        issue_books.remove(book_name)
        issue_books.append(books)
        print("Book return")
    else:
        print("blablabla")