

def get_choice(msg):
    return input(msg)

def get_and_validate(msg, validation):
    is_valid_input = False
    choice = ''
    while not is_valid_input:
        choice = get_choice(msg)
        is_valid_input = validation(choice)

    return choice