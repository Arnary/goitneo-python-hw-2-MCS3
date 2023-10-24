def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            if func.__name__ == "add_contact" or func.__name__ == "change_contact":
                return "Give me name and phone please."
            elif func.__name__ == "show_phone":
                return "Give me name please."

            return "Invalid command."
        except IndexError:
            return "You don't have any contacts yet."

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        return "Contact with this name already exists. Use the 'change' command if you want to update a contact."
    else:
        contacts[name] = phone
        return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts):
    name, = args
    if name in contacts.keys():
        return contacts[name]
    else:
        raise KeyError


@input_error
def show_all(contacts):
    contact_book = list()
    if contacts == {}:
        raise IndexError
    for name, phone in contacts.items():
        contact_book.append('|{:>15} : {:<17}|'.format(name, phone))
    return "\n".join(contact_book)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
