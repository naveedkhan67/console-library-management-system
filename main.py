from library_management_system import Book
from library_management_system import ReferanceBook
from library_management_system import FictionBook
from library_management_system import Library
from library_management_system import clear_terminal
from library_management_system import create_book
from library_management_system import search_book
from library_management_system import remove_book


def operate_library(library: Library):
    while True:

        print("------------Welcome------------")
        print(f"-------To {library.name} Library-------")
        print()
        print("Press 1 to list all books")
        print("Press 2 to add a book")
        print("Press 3 to search for a book")
        print("Press 4 to remove a book")
        print(f"Press 5 to quit {library.name} Library")
        print()
        c = input()

        if c == "1":
            library.display_all_books()
        elif c == "2":
            create_book(library)
            clear_terminal()
        elif c == "3":
            search_book(library)
        elif c == "4":
            remove_book(library)
            clear_terminal()
        elif c == "5":
            break

def main():
    lahore_library = Library("Lahore")
    karachi_library = Library("Karachi")

    while True:
        print("You have two libraries available. Kindly select one")
        print("1. Lahore Library")
        print("2. Karachi Library")
        print("3. Quit")
        s = input("Enter the number you want to select: ")

        if s == "1":
            clear_terminal()
            operate_library(lahore_library)

        elif s == "2":
            clear_terminal()
            operate_library(karachi_library)

        elif s == "3":
            break

        else:
            print("Wrong input. Kindly enter again")


if __name__ == "__main__":
    main()