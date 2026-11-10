from data import books
from menu import show_menu
from logic import get_books_by_author ,get_available_books ,return_book ,borrow_book , display_books, search_book, add_book
from validations_and_checks import is_exist ,is_digits, is_not_empty
from i_o import get_and_validate


def main():
    choice = ""
    while choice != "8":
        show_menu()
        choice = get_and_validate("Choose an option: ", is_digits)
        if choice == '1':
            display_books(books)
        elif choice == '2':
            name = get_and_validate("Enter book name: ", is_not_empty)
            print(search_book(books, name))
        elif choice == '3':
            name = get_and_validate("Enter book name: ", is_not_empty)
            author = get_and_validate("Enter auther name: ", is_not_empty)
            year = get_and_validate("Enter publication year: ", is_digits)
            add_book(books, name, author, int(year))
        elif choice == '4':
            book_id = get_and_validate("Enter book id: ", is_digits)
            borrow_book(books, int(book_id))
        elif choice == '5':
            book_id = get_and_validate("Enter book id: ", is_digits)
            return_book(books, int(book_id))
        elif choice == '6':
            print(get_available_books(books))
        elif choice == '7':
            auther = get_and_validate("Enter auther name: ", is_not_empty)
            print(get_books_by_author(books, author))
        else:
            print("choich must be 1-8")
if __name__=="__main__":
    main()
