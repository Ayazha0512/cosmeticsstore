class Item:
    def __init__(self, id,  name, description, price, quantity):
        self._id = id
        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity


    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        self._quantity = quantity

    def add_quantity(self, quantity):
        self._quantity += quantity

    def subtract_quantity(self, quantity):
        self._quantity -= quantity

    def quantity_minus(self):
        self._quantity -= 1

    def quantity_plus(self):
        self._quantity += 1

    def __str__(self):
        return f"Id: {self._id} Name: {self._name}, Description: {self._description}, Price: {self._price}, Quantity: {self._quantity}"

