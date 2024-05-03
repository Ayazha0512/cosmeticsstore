from SkinCareItem import SkinCareItem
from MakeupItem import MakeupItem
from Item import Item

class Catalog():
    def __init__(self, items=None):
        self.__items = items if items is not None else []

    def skin_care_catalog(self):
        skincare_items = []
        for item in self.__items:
            if isinstance(item, SkinCareItem):
                skincare_items.append(item)
        return skincare_items

    def makeup_catalog(self):
        makeup_items = []
        for item in self.__items:
            if isinstance(item, MakeupItem):
                makeup_items.append(item)
        return makeup_items

    def available_items(self, list):
        items = []
        for item in self.__items:
            if issubclass(type(item), Item):
                if item.get_quantity() > 0:
                    items.append(item)
        return items

    def print_catalog(self):
        if not self.__items:
            print('No items available')
            return
        for item in self.__items:
            if issubclass(type(item), Item):
                print(item)

    def print_list(self, list):
        for item in list:
            if issubclass(type(item), Item):
                print(item)

    def find_item(self, id):
        for item in self.__items:
            if item.get_id() == id:
                return item

    def item_minus(self, id):
        for i in range(len(self.__items)):
            if self.__items[i].get_id() == id:
                if issubclass(type(self.__items[i]), Item):
                    self.__items[i].quantity_minus()

    def add_item(self, item):
        if(isinstance(item, Item)):
            for i in range(len(self.__items)):
                if self.__items[i].get_id() == item.get_id():
                    print("item id ")
                    return
        self.__items.append(item)

    def remove_item(self, id):
        for i in range(len(self.__items)):
            if self.__items[i].get_id() == id:
                self.__items.pop(i)
                print('Item removed')
                return
        print('Item not found')