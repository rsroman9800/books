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
            isbn, title, author, genre, available_str = line.strip().split(",")
            available = True if available_str.strip() == "True" else False # Converts avaiable from a string to a boolean value  
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
    if index != -1 and book_list[index].get_available() == False:
        book_list[index].return_it() 
        book_title = book_list[index].get_title() 
        print(f"'{book_title}' with ISBN {isbn} successfully returned.") # If the book is found, return the book and get the title of it to print an appropriate message
    elif index != -1 and book_list[index].get_available() == True:
        book_title = book_list[index].get_title()
        print(f"'{book_title}' with ISBN {isbn} is not currently borrowed.") # Otherwise, if the book is not available, return an appropriate message.
    else:
        print("No book found with that ISBN.") # If the book is not found at all, print an appropriate message

""" Step 2g: Defining the add_book() function which has the parameter of book_list. The user inputs a new ISBN, title, author, and genre name from the user. It creates a new instance of Book 
and appends it to the list."""
def add_book(book_list):
    print()
    print("-- Add a book --") # Print add a book header
    # Allow the user to input the isbn, title, and author which are all stripped of any potential leading whitespaces
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ").strip()
    title = input("Enter title: ").strip()
    author = input("Enter author name: ").strip()
    genre_names = [genre.lower() for genre in Genre.GENRE_NAMES.values()]  # Creates a genre_names list, which coverts all genre values in the GENRE_NAMES dict to lowercase for use in the later code.
    
    genre_found = False # Creating a flag 
    while genre_found == False:
        genre = input("Enter genre: ").strip().lower()  # Converts input to lowercase and strips whitespace
        if genre in genre_names:  # If the genre input by the user is in genre_names, proceed with the loop
            genre_number = genre_names.index(genre)  # The genre key is obtained by finding the index of the genre input.
            book = Book(isbn, title, author, genre_number, True) # The book object using the Book class
            book_list.append(book) # The book is appended to the book_list
            print(f"'{title}' with ISBN {isbn} successfully added.")
            genre_found = True  # Set genre_found to True to exit the loop
        else:
            print("Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, Young Adult, Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry")  # Print available genres

""" Step 2h: Define the remove_book() function which has the parameter of book_list. It inputs an ISBN from the user and calls find_book_by_isbn(). 
If an index to a matching book was returned, removes the book from the list. Otherwise displays an appropriate message. """
def remove_book(book_list):
    print()
    print("-- Remove a book --") # Prints an approprirate header
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ").strip() # Enters an isbn from the user, stripping it of any whitespace
    index = find_book_by_isbn(book_list, isbn) # Calls the find_book_by_isbn() method
    if index != -1: # If the value was found in find_book_by_isbn, proceed with the loop
        book_title = book_list[index].get_title() 
        book_list.remove(book_list[index]) # Gets the title of the book based on its index and removes it from the book_list.
        print(f"'{book_title}' with ISBN {isbn} successfully removed.") # Print an appropriate message
    else:
        print("No book found with that ISBN.") # Print an appropriate message

""" Step 2i: Define the print_books() function which has the parameter of book_list (and print_header for formatting). It displays a book information heading, 
then iterates through the book list displaying each Book object on a separate line. """
def print_books(book_list, print_header=True):
    if print_header == True: # Using print_header flag to print the print book catalog header only if option 6 is selected
        print()
        print("-- Print book catalog --")
    print("ISBN           Title                     Author                    Genre                Availability")
    print("-------------- ------------------------- ------------------------- -------------------- ------------")
    for book in book_list:
        print(f"{book.get_isbn():<14} {book.get_title():<25} {book.get_author():<25} {book.get_genre_name():<20} {book.get_availability()}") # Formats the books to align with the header

""" Step 2j: Define the save_books() function which reveives the parameters of book_list and file_name. It iterates over the list, 
formatting a comma separated string containing each book’s attribute values. Writes each string as a separate line to the file and returns the number of books saved to the file. """
def save_books(book_list, file_name):
    num_books_saved = 0 # Initializes the num_books_saved at 0
    with open(file_name, "w") as f: # Opens the file for writing
        # For each student information in the list, the program formats it in the CSV format using the format_student() function, adds a space, and proceeds to the next student_info
        for book in book_list:
            f.write(f"{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre()},{book.get_available()}\n")
            num_books_saved += 1 # Adds every book to the book_list using the Book class and increases the num_books_saved by 1.
        return num_books_saved # Returns the number of books saved.

""" Step 2k: Defining the main() function """
def main():
    print("Starting the system ...") # Prints the appropriate starting message
    book_list = [] # Creates an empty book_list variable
    file_name = "" # Creates an empty file_name variable
    num_books, file_name = load_books(book_list, file_name) # load_books function is run, which also returns the num_books and file_name
    user_input = "" # Creates an empty user_input variable
    librarian_menu_selected = False # Creates a flag for the librarian menu option selection

    # Main menu options for general users
    main_menu_options = {
        "1": "Search for books",
        "2": "Borrow a book",
        "3": "Return a book",
        "0": "Exit the system"
    }
    
    # Librarian menu options
    librarian_menu_options = {
        "1": "Search for books",
        "2": "Borrow a book",
        "3": "Return a book",
        "4": "Add a book",
        "5": "Remove a book",
        "6": "Print catalog",
        "0": "Exit the system"
    }
    
    while user_input != "0": # Repeats the loop until the user inputs 0
        print() # Prints an empty line according to the formatting of the assignment
        if librarian_menu_selected == True:
            user_input = print_menu("Reader's Guild Library - Librarian Menu", librarian_menu_options) # If the librarian_menu is selected, print the librarian_menu_options
        else:
            user_input = print_menu("Reader's Guild Library - Main Menu", main_menu_options) # Otherwise, print the regular options
        
        if user_input == "2130":
            librarian_menu_selected = True # Changes the flag to true if the librarian_menu is selected
        elif user_input == "0": 
            print()
            print("-- Exit the system --\nBook catalog has been saved.\nGood Bye!")
            save_books(book_list, file_name) # If user input is 0, print an appropriate message, save the book_list to books.csv 
        elif user_input == "1": 
            print()
            print("-- Search for books --") # Print the approprirate message for the user
            search_value = input("Enter search value: ") # Allow the user to enter a search_value
            search_result = search_books(book_list, search_value) # Run the search_books() based on the search_value and return the search_result list
            if len(search_result) > 0:
                print_books(search_result, print_header=False) # If the search_result is not empty, print all the books that match the criteria using print_books()
            else:
                None # None if search_result is empty
        elif user_input == "2":
            borrow_book(book_list) # Runs the borrow_book() method if the user selects option 2
        elif user_input == "3": 
            return_book(book_list) # Runs the return_book() method if the user selects option 3
        elif librarian_menu_selected == True: # If 2130 was input, allow the user to enter options 4, 5, and 6
            if user_input == "4":
                add_book(book_list) # Runs the add_book() method if the user selects option 4
            elif user_input == "5":
                remove_book(book_list) # Runs the remove_book() method if the user selects option 5
            elif user_input == "6":
                print_books(book_list) # Runs the print_books() method if the user selects option 6
        else:
            print("Invalid option") # If the user doesn't input options 0-6, or if the user enters options 4-6 when 2130 was not input, return an "invalid option"

if __name__ == "__main__": # Runs the main function if the module is run directly
    main()