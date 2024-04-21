import os.path
import csv

from book import Book
from genre import genre_table

additional_menu = False


def find_book_by_isbn(books, isbn) -> Book:
    for book in books:
        if isbn in book.isbn:
            return book


def print_books(found):
    for book in found:
        print(book)


def add_book(books):
    isbn = input("Enter ISBN: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    genre_name = input("Enter Genre name: ")
    for gen_key in genre_table:
        if genre_table.get(gen_key) == genre_name:
            book = Book(isbn, title, author, gen_key, True)
            books.append(book)
            print("new book added.")
            return
    print("invalid Genre name.")


def find_value_in_dict(dictionary, value):
    for key in dictionary:
        if dictionary.get(key) == value:
            return key
    return None


def remove_book(books):
    isbn = input("Enter ISBN: ")
    book = find_book_by_isbn(books, isbn)
    if book is not None:
        books.remove(book)
        print(f"remove book {book.title} successfully!")
    else:
        print(f"Invalid ISBN {isbn}.")
    return


def save_books(books, filename) -> int:
    with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['isbn', 'title', 'author', 'genre', 'available']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writer.writeheader()
        for book in books:
            writer.writerow({'isbn': book.isbn,
                             'title': book.title,
                             'author': book.author,
                             'genre': book.genre,
                             'available': book.available})
    return len(books)


if __name__ == "__main__":
    __books = []
    __filename = ""
    while True:
        __filename = input("Please type file path and press enter: ")
        if os.path.isfile(__filename):
            break
        else:
            print(f"not found file '{__filename}', please check file path!")

    books_count = load_books(__books, __filename)
    print(f"file '{__filename}' processed, {books_count} record(s) loaded.")

    while True:
        task = print_menu()

        if task == "0":
            save_count = save_books(__books, __filename)
            print(f"{save_count} records saved.")
            print('System out!')
            break
        elif task == "1":
            search_criteria = input("Please input the key you search for:")
            found = search_book(__books, search_criteria)
            if len(found) > 0:
                print_books(found)
            else:
                print('not found')
        elif task == "2":
            borrow_book(__books)
        elif task == "3":
            return_book(__books)
        elif task == "2130":
            additional_menu = True
            continue
        elif additional_menu:
            if task == "4":
                add_book(__books)
            elif task == "5":
                remove_book(__books)
            elif task == "6":
                print_books(__books)