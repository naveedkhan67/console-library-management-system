import os


class Book:

    def __init__(self, title, author, isbn, total_pages, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_pages = total_pages
        self.price = price
        

    def display_details(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("ISBN: ", self.isbn)
        print("Total Pages: ", self.total_pages)
        print("Price: ", self.price)
        print()


class ReferanceBook(Book):

    def __init__(self, title, author, isbn, total_pages, price, type):
        self.type = type
        super().__init__(title, author, isbn, total_pages, price)
        

    def display_details(self):
        print("Referance Book")
        super().display_details()
        print("Type: ", self.type)
        print()


class FictionBook(Book):

    def __init__(self, title, author, isbn, total_pages, price, genre):
        self.genre = genre
        super().__init__(title, author, isbn, total_pages, price)
        

    def display_details(self):
        print('Fiction Book')
        super().display_details()
        print("Genre: ", self.genre)
        print()


class Library:

    def __init__(self, name):
        """
        This creates an empty dictionary everytime so that
        different libraries can be created.
        """
        self.books = {}
        self.name = name
        

    def add_book(self, book: Book):
        self.books[book.title] = book
        

    def display_all_books(self):
        if not self.books:
            print("Library is empty :( ")
            print()

        for key in self.books:
            self.books[key].display_details()
            

    def search(self, title) -> Book:
        book = self.books.get(title)
        return book
    

    def remove(self, title):
        self.books.pop(title)


def clear_terminal():
    os.system("clear")


def book_type_selection():
    """This lets you select the type of the book you want to create"""

    book_type = None
    while True:
        message_string = (
            "Press S to create simple book F for fiction and R for a Referance book: "
        )
        book_type = input(message_string)
        book_type = book_type.lower()
        if book_type == "f" or book_type == "r" or book_type == "s":
            return book_type
        else:
            print("Invalid input")


def create_book(library: Library):
    book_type = book_type_selection()
    clear_terminal()

    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")

    while True:
        try:
            total_pages = int(input("Enter the total pages of the book: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid Number. \n")

    while True:
        try:
            price = int(input("Enter the price the book: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid Number. \n")

    book = None

    if book_type == "s":
        book = Book(title, author, isbn, total_pages, price)
    elif book_type == "r":
        type = input("Please enter the type of the book: ")
        book = ReferanceBook(title, author, isbn, total_pages, price, type)

    elif book_type == "f":
        genre = input("Please enter the genre of the book: ")
        book = FictionBook(title, author, isbn, total_pages, price, genre)

    library.add_book(book)
    print("Book added Successfully")


def search_book(library: Library):
    title = input("Enter the title that you want to search: ")

    book = library.search(title)
    if book:
        book.display_details()
    else:
        print("Book not found")


def remove_book(library: Library):
    title = input("Enter the title that you want to remove")
    book = library.search(title)
    if book:
        library.remove(book.title)
    else:
        print("Book not found :(")




