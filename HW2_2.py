from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if any((not value.isdigit(), len(value) != 10)):
            raise ValueError("Phone is in the wrong format.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        for idx, abook_phone in enumerate(self.phones):
            if str(abook_phone) == phone:
                self.phones.pop(idx)
                break

    def edit_phone(self, old_phone, new_phone):
        for idx, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[idx] = Phone(new_phone)

    def find_phone(self, phone):
        for abook_phone in self.phones:
            if str(abook_phone) == phone:
                return phone
        return "Phone not found"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]
