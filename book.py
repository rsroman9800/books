from genre import genre_table


class Book(object):
    # __isbn = ''
    # __title = ''
    # __author = ''
    # __genre = 0
    # __available = False
    @property
    def isbn(self):
        return self.__isbn

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    @property
    def available(self):
        return self.__available

    def __init__(self, isbn, title, author, genre, available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = available

    def get_genre_name(self):
        return genre_table[self.__genre]

    def get_availability(self):
        return self.__available

    def borrow_it(self):
        self.__available = False

    def return_it(self):
        self.__available = True

    # def __str__(self):
    #     return 'ISBN: {}, Title: {}, Author: {}, Genre: {}, Available: {}'.format(self.__isbn,
    #                                                                               self.__title,
    #                                                                               self.__author,
    #                                                                               self.get_genre_name(),
    #                                                                               self.__available)
