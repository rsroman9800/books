"""
Name: Book Class
Description: Defines the properties/attributes and methods of the book class.
Properties/Attributes:
- isbn (private): ISBN number of the book.
- title (private): Title of the book.
- author (private): Author of the book.
- genre (private): Genre of the book represented as an integer.
- available (private): Availability status of the book, either True or False.

Methods:
- Constructor: Initializes all 5 attributes to the corresponding values passed in.
- Getters: Standard getters for isbn, title, author, genre, and availability.
- get_genre_name(): Getter method that returns the name of the genre as a string.
- get_availability(): Getter method that returns a string indicating availability status.
- Setters: Standard setter methods for isbn, title, author, and genre.
- borrow_it(): Sets the book’s available attribute to False.
- return_it(): Sets the book’s available attribute to True.
- str(): Returns a string representation of the book formatted for display.
Authors: Roman Sorokin, Yaling Wei
Date: March 29, 2024
"""

# Step 1a: Create the Genre class which includes the key-value dictionary of GENRE_NAMES and initalizes the genre_code variable
class Genre:
    def __init__(self, genre_code):
        self.genre_code = genre_code
    
    GENRE_NAMES = {
        0: "Romance",
        1: "Mystery",
        2: "Science Fiction",
        3: "Thriller",
        4: "Young Adult",
        5: "Children's Fiction",
        6: "Self-help",
        7: "Fantasy",
        8: "Historical Fiction",
        9: "Poetry"
    }

# Step 1b: Create the Book class which initalizes the isbn, title, author, genre, and available variables.
class Book:
    def __init__(self, isbn, title, author, genre, available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = int(genre)
        self.__available = bool(available)
    
    # Step 1b.i: Define getters
    def get_isbn(self):
        return self.__isbn
   
    def get_title(self):
        return self.__title
   
    def get_author(self):
        return self.__author
   
    def get_genre(self):
        return self.__genre
   
    def get_available(self):
        return self.__available
   
    # Gets the genre name from the GENRE_NAMES based on the genre_code provided
    def get_genre_name(self):
        return Genre.GENRE_NAMES.get(self.__genre, "N/A")
    
    # If available is true, return "Available" string, otherwise, return the "Borrowed" string
    def get_availability(self):
        return "Available" if self.__available == True else "Borrowed"
    
    # Step 1b.ii: Define setters
    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn
   
    def set_title(self, new_title):
        self.__title = new_title
   
    def set_author(self, new_author):
        self.__author = new_author
   
    def set_genre(self, new_genre):
        self.__genre = new_genre
    
    # Sets availability to False
    def borrow_it(self):
        self.__available = False
    
    # Sets availability to True
    def return_it(self):
        self.__available = True
   
    # Step 1b. iii: Define how the information wil be displayed through the string method
    def __str__(self):
        return f"{self.__isbn} {self.__title:<25} {self.__author:<25} {self.get_genre_name():<20} {self.get_availability()}"