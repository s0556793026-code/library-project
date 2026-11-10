

def is_digits(choice):
    if choice.isdigit():
        return True
    print("choice must be an integer")
    return False

def is_not_empty(choice):
    if choice.strip():
        return True
    print("choice cannot be empty")
    return False

def is_exist(books, value, type_value):
    for book in books:
        if book[type_value] == value:
            return True
    print("book is not exist")
    return False
