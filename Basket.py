from Catalog import Catalog
from Client import Client

class Basket:
    def __init__(self):
        self.items = []
        self.quantity = 0
        self.total_price = 0

    def add_item(self, id, catalog: Catalog):
        item = catalog.find_item(id)
        if item is None:
            print('Item not found')
            return
        if item.get_quantity() > 0:
            self.quantity +=1
            self.total_price += item.get_price()
            self.items.append(item)
        print("item with id {} added".format(id))

    def remove_item(self, id):

        for item in self.items:
            if item.get_id() == id:
                self.items.remove(item)
                self.quantity -=1
                self.total_price -= item.get_price()
                print("item with id {} removed".format(id))
                return
        print("Item with id {} not found".format(id))

    def buy_item(self, catalog: Catalog, client:Client):
        if client is None:
            print("Client is None")
            return
        if(client.get_balance() < self.total_price):
            print("You don't have enough money!")
            return

        for item in self.items:
            catalog.item_minus(item.get_id())
            client.set_balance(client.get_balance() - item.get_price())
            self.items = []
            self.quantity = 0
            self.total_price = 0
            print("Payment is made. Success!")

    def show__basket(self):
        for item in self.items:
            print(item)
        print("Total price: {}".format(self.total_price))