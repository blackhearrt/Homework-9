CONTACTS_DICT = {}

# Створення функції для "перехоплення" помилок.
def input_error(func):
    def errors(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError. Enter username."
        except ValueError:
            return "ValueError. Enter username and phone number."
        except IndexError:
            return "IndexError. Enter username and phone number."
    return errors


# Створення декоратора для функції додавання імені та телефонного номеру до словника.
@input_error
def add_contacts(name, phone):
    if name in CONTACTS_DICT:
        raise ValueError
    CONTACTS_DICT[name] = phone
    return f"{name.title()} contact with number {phone} has been added."


# Створення декоратора для функції, що заміняє телефонний номер абонента на інший.
@input_error
def change_phone(name, phone):
    if name not in CONTACTS_DICT:
        raise KeyError
    else:
        CONTACTS_DICT[name] = phone
        return f"Phone number for {name.title()} contact has been changed to {phone}."


# Отримання номеру телефону з імені відповідного контакту.
@input_error
def get_phone(name):
    if name not in CONTACTS_DICT:
        raise KeyError
    return f"{name.title()}'s phone number is: {CONTACTS_DICT[name]}."


# Отримання рядку зі всіма контактами із словника.
@input_error
def show_all():
    if not CONTACTS_DICT:
        raise KeyError
    result = f"List of all contacts:\n"
    for name, phone in CONTACTS_DICT.items():
        result += f"{name.title()}: {phone} \n"
    return result


def hello():
    return "Hi, how can I help you?"


def end():
    return "Goodbye!"


# Створення основної функції для обробки команд та інших функцій.
def main():
    while True:
        user_input = input("Enter a command: ").lower()
        user_separated = user_input.split(maxsplit=2)
        result_input = ""

        for char in user_input:
            if char != " ":
                result_input += char
            else:    
                break

        if user_input in ["hello", "hi", "good morning", "good evening"]:
            print(hello())

        elif result_input == "add":
            if len(user_separated) < 3:
                print("Enter <add> <user_name> <phone_number> please.")
            else:
                print(add_contacts(user_separated[1], user_separated[2]))

        elif result_input == "change":
            if len(user_separated) < 3:
                print("Enter <change> <user_name> <phone_number> please.")
            else:
                print(change_phone(user_separated[1], user_separated[2]))

        elif result_input == "phone":
            if len(user_separated) < 2:
                print("Enter <phone> <user_name> please.")
            else:
                print(get_phone(user_separated[1]))

        elif user_input == "show all":
            print(show_all())

        elif user_input in ["goodbye", "close", "exit"]:
            print(end())
            break

        else:
            print("Unknown command. Try this instead: 'hello', 'hi', 'good morning', 'good evening', 'add', 'change',"
                  " 'phone', 'show all', 'goodbye', 'close', 'exit'.")
        

if __name__ == '__main__':
    main()