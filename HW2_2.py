from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def is_valid(self):
        if self.value.isdigit() and len(self.value) == 10:
            return True
        else:
            print("Phone is in the wrong format.")
            return False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        if Phone(phone).is_valid():
            self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for idx, abook_phone in enumerate(self.phones):
            if abook_phone.__str__() == phone:
                self.phones.pop(idx)
                break

    def edit_phone(self, old_phone, new_phone):
        if Phone(new_phone).is_valid():
            for idx, phone in enumerate(self.phones):
                if phone.__str__() == old_phone:
                    self.phones[idx] = Phone(new_phone)

    def find_phone(self, phone):
        for abook_phone in self.phones:
            if abook_phone.__str__() == phone:
                return phone
        return "Phone not found"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.__str__()] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

