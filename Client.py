
class Client:
    def __init__(self, name, phone, balance):
        self.__name = name
        self.__phone = phone
        self.__balance = balance

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def __str__(self):
        return f'{self.__phone} . {self.__name}: {self.__balance}'
