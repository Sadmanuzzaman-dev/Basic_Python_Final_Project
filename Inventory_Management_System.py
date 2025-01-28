#import json


class Inventory:
    def __init__(self):
        self.inventory = {}
        # with open("data.txt", "r") as file:
        #     self.inventory = json.load(file)

    def add_item(self, item_name, stock_count, price):
        self.inventory[item_name] = {"stock_count": stock_count, "price": price}
        # with open("data.txt", "w") as file:
        #     json.dump(self.inventory, file)

    def update_item(self, item_name, stock_count, price):
        if item_name in self.inventory:
            self.inventory[item_name]["stock_count"] = stock_count
            self.inventory[item_name]["price"] = price
        else:
            print("Item not found in inventory.")

    def check_item_details(self, item_name):
        if item_name in self.inventory:
            item = self.inventory[item_name]
            return f"Product Name: {item_name}, Stock Count: {item['stock_count']}, Price: {item['price']}"
        else:
            return "Item not found in inventory."

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]

        else:
            print("Item not found in inventory.")


def main():
    inventory = Inventory()
    Run = True

    while Run:
        print(" Write 1 to Add item")
        print(" Write 2 to Update item")
        print(" Write 3 to Check item details")
        print(" Write 4 to Remove item")
        choice = int(input("What you want to do?: "))

        if choice == 1:
            product_name = input("Product Name: ")
            product_stock = input("Product Stock: ")
            product_price = input("Product Price: ")
            inventory.add_item(product_name, product_stock, product_price)

        elif choice == 2:
            product_name = input("Product Name: ")
            product_stock = input("Product Stock: ")
            product_price = input("Product Price: ")
            inventory.update_item(product_name, product_stock, product_price)

        elif choice == 3:
            product_name = input("Product Name: ")
            print(inventory.check_item_details(product_name))

        elif choice == 4:
            product_name = input("Product Name: ")
            inventory.remove_item(product_name)

        else:
            Run = False


main()
