class Genre:
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
   
    def __init__(self, genre_code):
        self.genre_code = genre_code

class Book:
    def __init__(self, isbn, title, author, genre, available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = int(genre)
        self.__available = bool(available)
    
    # Define getters
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
   
    def get_genre_name(self):
        return Genre.GENRE_NAMES.get(self.__genre, "N/A")
   
    def get_availability(self):
        return "Available" if self.__available == True else "Borrowed"
    
    # Define setters
    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn
   
    def set_title(self, new_title):
        self.__title = new_title
   
    def set_author(self, new_author):
        self.__author = new_author
   
    def set_genre(self, new_genre):
        self.__genre = new_genre
   
    def borrow_it(self):
        self.__available = False
   
    def return_it(self):
        self.__available = True
   
    # Define how the information wil be displayed
    def __str__(self):
        return f"{self.__isbn} {self.__title:<25} {self.__author:<25} {self.get_genre_name():<20} {self.get_availability()}"