
def display_books(books):
    for book in books:
        print(book)


def search_book(books, name):
    books_choice = []
    for book in books:
         if name.lower() in book.get("name").lower():
            books_choice.append(book)
    if not books_choice:
        return None
    return books_choice

def add_book(books, name, author, year):
    for book in books:
        if book["name"] == name and book["auther"] == author:
            return False
    books.append({"id": get_next_book_id(books), 
                "name": name,
                "author": author,
                "year": year,
                "available": True
                })
    return True

def borrow_book(books, book_id):
    for book in books:
        if book_id == book["id"]:
            if book["available"] == True:
                book["available"] = False
                print("Book borrowed successfully.")
                return True
            print("The book is already on loan.")
            return False
    print("Book is not exist.")
    return False

def return_book(books, book_id):
    for book in books:
        if book_id == book["id"]:
            if book["available"] == False:
                book["available"] = True
                print("Book returned successfully.")
                return True
            print("Book was not borrowed")
            return False
    print("Book is not exist.")
    return False

def get_available_books(books):
    available_books = []
    for book in books:
        if book["available"] == True:
            available_books.append(book["name"])
    return available_books

def get_books_by_author(books, author):
    for book in books:
        if book["author"].lower() == author.lower():
            return list(book.items())
    return "book in not exist"
    
def get_next_book_id(books):
    return books[-1]["id"]+ 1


