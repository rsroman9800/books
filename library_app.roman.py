# Step 1: Import os module
import os
from book import Book
from book import Genre

# Step 2a: Defining the load_books() function
def load_books(book_list, file_name):
    file_name = input("Enter book catalog filename: ")
    num_books = 0
    # Checks if the file exists. If it does, it opens the file, reads each line, and then appends it to the book_list variable, 
    # stripping the line of any leading/trailing white spaces and splitting each string in the list using commas. It then returns the book_list
    while not os.path.exists(file_name):
        file_name = input("File not found. Re-enter book catalog filename: ")
    print("Book catalog has been loaded.")
    with open(file_name, "r") as f:
        for line in f:
            isbn, title, author, genre, available = line.strip().split(",")
            book = Book(isbn, title, author, genre, available)
            book_list.append(book)
            num_books += 1
    return num_books, file_name

# Step 2b: Defining the print_menu() function
def print_menu(menu_heading, menu_options):
    # Displays menu heading
    print(menu_heading)
    print("=" * len(menu_heading))
    # Displays menu options
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    # Input selection from user until valid selection is entered
    valid_selection = False
    while valid_selection == False:
        user_input = input("Enter your selection: ").strip()
        if user_input in menu_options or user_input == "2130":
            valid_selection = True
            return user_input
        else:
            print("Invalid option")
            
# Step 2c.i: Defining the matches_search_criteria() function for the search_books() function
def matches_search_criteria(book, search_value):
    search_attributes = [book.get_isbn().lower(), book.get_title().lower(), book.get_author().lower(), book.get_genre_name().lower()]
    for attribute in search_attributes:
        if search_value.lower() in attribute:
            return True
    return False

# Step 2c.ii: Defining the search_books() function
def search_books(book_list, search_value):
    search_result = []
    for book in book_list:
        if matches_search_criteria(book, search_value) == True:
            search_result.append(book)
    if search_result == []:
        print("No matching books found.")
    return search_result

# Step 2d: Define the borrow_book() function
def borrow_book(book_list):
    print()
    print("-- Borrow a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)
    if index != -1 and book_list[index].get_available() == True:
        book_list[index].borrow_it()
        book_title = book_list[index].get_title()
        print(f"'{book_title}' with ISBN {isbn} successfully borrowed.")
    elif index != -1 and book_list[index].get_available() == False:
        book_title = book_list[index].get_title()
        print(f"'{book_title}' with ISBN {isbn} is not currently available.")
    else:
        print("No book found with that ISBN.")

# Step 2e: Define the find_book_by_isbn() function
def find_book_by_isbn(book_list, isbn):
    for i in range(len(book_list)):
        if book_list[i].get_isbn() == isbn:
            return i
    return -1
        
# Step 2f: Define the return_book() function
def return_book(book_list):
    print()
    print("-- Return a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)
    if index != -1 and book_list[index].get_available() == True:
        book_list[index].return_it()
        book_title = book_list[index].get_title()
        print(f"'{book_title}' with ISBN {isbn} successfully returned.")
    elif index != -1 and book_list[index].get_available() == False:
        book_title = book_list[index].get_title()
        print(f"'{book_title}' with ISBN {isbn} is not currently borrowed.")
    else:
        print("No book found with that ISBN.")