from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
       return str(self.value)

class Name(Field):
    # Клас для зберігання імені контакту. Обов'язкове поле.
		pass

class Phone(Field):
    # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, value):
         super().__init__(value)
         self.value = self.phonevalid(self.value)       

    def phonevalid(self, numer):
        if len(numer) == 10:
            for count in numer:
                if count.isdigit():
                    okay = True
                else:
                    okay = False
                    break
        else:
            okay = False
        if okay:    
            return numer
        else:
            return "Nope:)"
        

class Record:
    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    
    def add_phone(self, phone):
        # метод для додавання об'єктів Phone
        self.phone = Phone(phone)   #obj
        if self.phone.value != "Nope:)":
            self.phones.append(self.phone)
    

    def remove_phone(self, phone):
        # метод для видалення об'єктів Phone
        self.phone = phone      #str        
              
        for p in self.phones:
            if p.value == self.phone:
                self.phones.remove(p)


    def edit_phone (self, old_phone, new_phone):
        # метод для редагування об'єктів Phone
        self.old_phone = old_phone      # str
        self.new_phone = new_phone      # str
        
        for p in self.phones:
            if p.value == self.old_phone:
                p.value = self.new_phone


    def find_phone (self, fnd_phone):
        # метод для пошуку об'єктів Phone
        self.fnd_phone = fnd_phone      #str

        for p in self.phones:
            if p.value == self.fnd_phone:
                findet_phone = p.value

        return findet_phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

        
class AddressBook(UserDict):
    # реалізація класу
	
    def add_record(self, recording):
    # метод add_record, який додає запис до self.data
        self.key = recording.name.value
        self.value = recording
        self.data[self.key] = self.value

    def find(self, name_fnd):
    # метод find, який знаходить запис за ім'ям
        self.name_fnd = name_fnd
        return self.data.get(self.name_fnd)

    def delete(self, name_del):
    # метод delete, який видаляє запис за ім'ям
        self.name_del = name_del
        del self.data[self.name_del]



if __name__ == '__main__':

    # Створення нової адресної книги
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
    print (book)
    # Видалення запису Jane
    book.delete("Jane")
    

