"""
Name: Library Management Module
Description: Upon start-up, load all library books from a CSV file into a list. Allow general users to select and perform any of the following main menu functions 
(continuously until the user chooses to exit the system):
1.	Search for books
2.	Borrow a book
3.	Return a book
0.	Exit the system
Entry of the special passcode of “2130” unlocks additional menu options, allowing librarian users to also select and perform the following librarian menu functions:
4.	Add a book
5.	Remove a book
6.	Print catalog
Upon shut-down, save all library books from the list to the CSV file.
Authors: Roman Sorokin, Yaling Wei
Date: March 29, 2024
"""

# Step 1: Import os module
import os
from book import Book
from book import Genre

""" Step 2a: Defining the load_books() function which creates Book objects from each set of attributes and adds them one-by-one onto the list with the parameters of book_list and file_name. 
It returns the number of books and the filename. """
def load_books(book_list, file_name):
    file_name = input("Enter book catalog filename: ") # Allows the user to input the filename
    num_books = 0 # num_books counter
    while not os.path.exists(file_name): 
        file_name = input("File not found. Re-enter book catalog filename: ") # If os.path does not exist, loop until the user enters a proper filename
    print("Book catalog has been loaded.")
    with open(file_name, "r") as f:
        for line in f:
            # For every line in the file, strip of any leading or trailing white spaces, and split each value separated by a comma into the 5 categories
            isbn, title, author, genre, available = line.strip().split(",")  
            book = Book(isbn, title, author, genre, available) # Create a book object using the book class and the values created earlier
            book_list.append(book) # Append the book to the book list
            num_books += 1 # Add 1 to the num_books per each book added
    return num_books, file_name # Return the num_books and the filename

""" Step 2b: Defining the print_menu() function which displays the heading and menu options passed in (parameters: menu_heading, menu_options), inputs selection from user until 
a valid selection is entered, and returns the user’s valid selection. """
def print_menu(menu_heading, menu_options):
    # Displays menu heading based on the entry of the user
    print(menu_heading)
    print("=" * len(menu_heading))
    # Displays menu options from the dictionary list given based on the user's selection
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    # Input selection from user until valid selection is entered
    valid_selection = False # valid_selection flag
    while valid_selection == False:
        user_input = input("Enter your selection: ").strip()
        if user_input in menu_options or user_input == "2130": # If user inputs a valid option in the menu_options or enters the librarian code, it returns a valid selection
            valid_selection = True
            return user_input
        else:
            print("Invalid option") # Else, user picked an invalid option and they must enter a valid selection
            
""" Step 2c.i: Defining the matches_search_criteria() function for the search_books() function that takes in the book and search_value parameters and returns 
either True or False if the book matches the search criteria """
def matches_search_criteria(book, search_value):
    search_attributes = [book.get_isbn().lower(), book.get_title().lower(), book.get_author().lower(), book.get_genre_name().lower()] # Sets all the attributes to lowercase of each book 
    for attribute in search_attributes:
        if search_value.lower() in attribute: # Search value entered by user is converted to lowercase and checks if it is in any attribute 
            return True
    return False

""" Step 2c.ii: Defining the search_books() function which has the parameters of book_list and search_value. It iterates through the list of books and checks if the search string appears in isbn, title, author, or genre name. 
If any match is found, the book is added to the search result list. It returns search result list """
def search_books(book_list, search_value):
    search_result = [] # Creating an empty search_result list
    for book in book_list:
        if matches_search_criteria(book, search_value) == True: 
            search_result.append(book) # If any value entered by the user matches a book attrbiute, it is appended to the search_result list
    if search_result == []:
        print("No matching books found.") # Otherwise, if the search_result remains empty, an appropriate message is displayed
    return search_result

""" Step 2d: Defining the borrow_book() function which takes the parameter of book_list. Inputs an ISBN from the user and calls find_book_by_isbn(). If an index to a matching book was 
returned and that book is currently available, invokes the book's borrow_it() method. Otherwise displays an appropriate message. """
def borrow_book(book_list):
    print() # Prints and empty row for styling
    print("-- Borrow a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ") # Requests the user enter and ISBN
    index = find_book_by_isbn(book_list, isbn) # Calls the find_book_by_isbn function
    if index != -1 and book_list[index].get_available() == True: 
        book_list[index].borrow_it() 
        book_title = book_list[index].get_title() 
        print(f"'{book_title}' with ISBN {isbn} successfully borrowed.") # If the book was found run the borrow_it() setter and get the book's title to print an appropriate message
    elif index != -1 and book_list[index].get_available() == False:
        book_title = book_list[index].get_title()
        print(f"'{book_title}' with ISBN {isbn} is not currently available.") # If the book is not available, print an appropriate message
    else:
        print("No book found with that ISBN.") # If the book is not found at all, print an appropriate message

""" Step 2e: Defining the find_book_by_isbn() function which has the parameters of book_list and isbn. It iterates through the list of books and compares the ISBN parameter to each book's isbn. 
Iteration stops when an exact match is found or when the end of the list is reached. Returns the index of the matching book or -1 if none found. """
def find_book_by_isbn(book_list, isbn):
    for i in range(len(book_list)):
        if book_list[i].get_isbn() == isbn: 
            return i # For every book in the book_list, if the isbn matches a book in the book list, return the index of that book for the borrow_book() method
    return -1 # If no book is matched with the isbn, return a -1 which indicates that a specific value was not found
        
""" Step 2f: Defining the return_book() function which has the parameter of a book_list. It inputs an ISBN from the user and calls find_book_by_isbn(). If an index to a matching book was returned 
and that book is currently borrowed, invokes the book’s return_it() method. Otherwise displays an appropriate message. """
def return_book(book_list):
    print() # Print an empty row for styling
    print("-- Return a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ") # Receive an isbn input from the user.
    index = find_book_by_isbn(book_list, isbn)
    if index != -1 and book_list[index].get_available() == True:
        book_list[index].return_it() 
        book_title = book_list[index].get_title() 
        print(f"'{book_title}' with ISBN {isbn} successfully returned.") # If the book is found, return the book and get the title of it to print an appropriate message
    elif index != -1 and book_list[index].get_available() == False:
        book_title = book_list[index].get_title()
        print(f"'{book_title}' with ISBN {isbn} is not currently borrowed.") # Otherwise, if the book is not available, return an appropriate message.
    else:
        print("No book found with that ISBN.") # If the book is not found at all, print an appropriate message
