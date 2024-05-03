from Catalog import Catalog
from Basket import Basket
from MakeupItem import MakeupItem
from Client import Client
from SkinCareItem import SkinCareItem


class CosmeticsStore:

    def __init__(self):
        self.__clients = []
        self.__catalog = Catalog()

    def get_clients(self , phone):
        for client in self.__clients:
            if client.get_phone() == phone:
                return client
        print("client not found")

    def add_client(self, client:Client):
        if client not in self.__clients:
            self.__clients.append(client)
            print("client added")
            return
        print("client already added")

    def all_clients(self):
        clients = []
        for client in self.__clients:
            clients.append(client)
        return clients

def display_menu():
    print("                                                ")
    print("---------------Cosmetics Controller---------------")
    print("1. Client panel")
    print("2. Admin panel")
    print("0. Exit")

def main():
    controller = CosmeticsStore()
    catalog = Catalog()
    basket = Basket()

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                phone = int(input("Enter your phone: "))
                client = controller.get_clients(phone)
                if client is None:
                    print("Go to admin page and register your client")
                else:
                    print(f"Welcome to out store,{client.get_name()}")
                    while True:
                        try:
                            print("----------------------------")
                            print("1. Show catalog")
                            print("2. Add item to basket")
                            print("3. Remove item from basket")
                            print("4. show basket")
                            print("5. buy")
                            print("6. exit")
                            print("----------------------------")
                            choice = input("Enter your choice: ")
                            if (choice == "1"):
                                catalog.print_catalog()
                            elif (choice == "2"):
                                id = int(input("Enter item id: "))
                                basket.add_item(id, catalog)
                            elif (choice == "3"):
                                id = int(input("Enter item id: "))
                                basket.remove_item(id)

                            elif (choice == "4"):
                                basket.show__basket()

                            elif (choice == "5"):

                                basket.buy_item(catalog, client)

                            elif (choice == "6"):
                                break
                        except ValueError:
                            print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input")

        if choice == "2":
            while True:
                try:
                    print("----------------------------")
                    print("1. Show catalog")
                    print("2. Add item to catalog")
                    print("3. Remove item from catalog")
                    print("4. Add client")
                    print("5. Show client")
                    print("6. exit")
                    print("----------------------------")
                    choice = input("Enter your choice: ")
                    if(choice == "1"):
                        catalog.print_catalog()
                    elif (choice == "2"):
                        while True:
                            print("----------------------------")
                            print("1.Add makeup item")
                            print("2.Add skincare item")
                            print("3.exit")
                            print("----------------------------")

                            type = int(input("Enter type of item: "))
                            if type == 1:
                                id = int(input("Enter item id: "))

                                name = input("Enter name: ")
                                while name.strip() == "":
                                    name = input("Enter name: ")

                                description = input("Enter description: ")
                                while description.strip() == "":
                                    description = input("Enter description: ")
                                price = int(input("Enter price: "))
                                quantity = int(input("Enter quantity: "))
                                shade = int(input("Enter shade: "))
                                makeup = MakeupItem(id, name, description, price, quantity, shade)
                                catalog.add_item(makeup)
                            elif type == 2:
                                id = int(input("Enter item id: "))
                                name = input("Enter name: ")
                                while name.strip() == "":
                                    name = input("Enter name: ")
                                description = input("Enter description: ")
                                while description.strip() == "":
                                    description = input("Enter description: ")
                                price = int(input("Enter price: "))
                                quantity = int(input("Enter quantity: "))
                                area = (input("Enter area: "))
                                while area.strip() == "":
                                    area = input("Enter area: ")
                                skincare = SkinCareItem(id, name, description, price, quantity, area)
                                catalog.add_item(skincare)
                            elif type == 3:
                                break
                    elif (choice == "3"):
                        id = int(input("Enter item id: "))
                        catalog.remove_item(id)
                    elif (choice == "4"):
                        name = input("Enter name: ")
                        while name.strip() == "":
                            name = input("Enter name: ")
                        phone = int(input("Enter phone number: "))
                        balance = int(input("Enter balance: "))
                        human = Client(name, phone, balance)
                        controller.add_client(human)
                    elif (choice == "5"):
                        if controller.all_clients() ==[]:
                            print("No clients")
                        for client in controller.all_clients():
                            print(client)

                    elif (choice == "6"):
                        break
                except ValueError:
                    print("Invalid input. Try again.")
        if choice == "0":
            print("Thank you for using CosmeticsStore!")
            break

if __name__ == "__main__":
    main()
# register for client by ownself

# add deposit in client section

