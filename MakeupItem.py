from Item import Item

class MakeupItem(Item):
    def __init__(self, id, name, description, price, quantity, shade):
        super().__init__(id, name, description, price, quantity)
        self.__shade = shade

    def get_shade(self):
        return self.__shade

    def set_shade(self, shade):
        self.__shade = shade


    def __str__(self):
        return f"Id:{self._id} Name: {self._name}, Description: {self._description}, Price: {self._price}, Quantity: {self._quantity}, Shade: {self.__shade}"
