from Item import Item

class SkinCareItem(Item):
    def __init__(self, id, name, description, price, quantity, area):
        super().__init__(id, name, description, price, quantity)
        self.__area = area

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area

    def __str__(self):
        return f"Id:{self._id} Name: {self._name}, Description: {self._description}, Price: {self._price}, Quantity: {self._quantity}, Area: {self.__area}"