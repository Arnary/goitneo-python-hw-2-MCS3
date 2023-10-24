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


book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
# Додавання запису John до адресної книги
book.add_record(john_record)
# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)
# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
# Видалення запису Jane
book.delete("Jane")
for name, record in book.data.items():
    print(record)
