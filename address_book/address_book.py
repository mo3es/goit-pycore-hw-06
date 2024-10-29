from collections import UserDict


"""
    This programm provides managing of contacts.
    Class address_book is manager - class, that provides creating, storing, deleting and finding contacts - by using functions with same names
    Record class is an entity, that stores info about user`s name, phone numbers, etc. Its provides creation, phone number adding, deleting and changing, etc.

"""


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_instance = Phone(phone)
        if phone not in [p.value for p in self.phones]:
            self.phones.append(phone_instance)
            print(f"Inputed phone number {phone} successfully added")
        else:
            print(f"Inputed phone number {phone} already exists")

    def del_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                print(f"Inputed phone number {phone} successfully deleted")
                return
        print(f"Inputed phone number {phone} doesn`t exist")

    def edit_phone(self, phone, new_phone):
        for p in self.phones:
            if p.value == phone:
                if new_phone not in [p.value for p in self.phones]:
                    p.value = new_phone
                    print(
                        f"Inputed phone number {phone} successfully edited to {new_phone}"
                    )
                else:
                    print(
                        f"Phone number {new_phone} already exists, phone number {phone} was not edited"
                    )
                return

    def find_phone(self, phone):
        if phone in [p.value for p in self.phones]:
            print(f"In {self.name.value} contact info, phone number {phone} exists")
        else:
            print(
                f"In {self.name.value} contact info, phone number {phone} does not exist"
            )

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record: Record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record
            print(f"Record {record.name.value} was successfully added")
        else:
            print(f"Record {record.name.value} already exists")

    def find(self, name) -> Record:
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Record of person {name} was successfully deleted")
        else:
            print(f"Record for person {name} not found")
