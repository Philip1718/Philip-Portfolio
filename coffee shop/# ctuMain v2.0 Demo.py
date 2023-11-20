<<<<<<< HEAD
version https://git-lfs.github.com/spec/v1
oid sha256:305616098ed748534bc9bc8aae5a60ae0e00dec04e565ba5faaecd55c7927735
size 5704
=======
# ctuMain.py:

#I Import class ctuStock from ctuClass file.
import sys
sys.path.append(".")
from ctuClass import ctuStock

# The items currently in stock with their price and quantity.
ctuStock.stock = {
    "Ruby Bluetooth Speaker": [10.00, 100],
    "Valkano Headphones": [20.50, 50],
    "Knobi Wallet": [5.25, 200],
    "Bentec Watch": [8.70, 75],
}
# The following shops that have the items in stock.
# If one shop is out of stock, its possible to try another shop 
shop1 = ctuStock()
shop2 = ctuStock()
shop3 = ctuStock()
shop4 = ctuStock()

Shopname = [shop1, shop2, shop3, shop4]

# Main Menu of the Program
# The user will be prompt to choose an option or exit the program
def main_menu():
    print()
    print("1. Shop Management")
    print("2. Sales")
    print("3. Returns")
    print("4. Stock")
    print("99. Exit")

# If user selects the first option Shop Management, this will be displayed
# The user will be prompt to choose where they want to go or back to main menu
def option1():
    while True:
        print()
        print("1. Change Shop Name")
        print("2. Change Shop Location")
        print("3. Display current shops")
        print("4. Display all shops information")
        print("0. Back")
        print()
        choice = input("Select an option: ")    # An input for the user to make a choice
        print()
        if choice == "1":
            display_shops() # If the user entered "1", current or unnamed shops will appear
            shop_index = select_shop() # They will be able to choose what shops name to change, one at a time 
            new_name = input("Enter new shop name: ") # The user will input the new name of the shop
            if Shopname[shop_index].change_shop_name(new_name): # If the shopname = to shopname[index], the name will change.
                print("Shop name changed successfully!") # and a message confirming the name has changed.
            else:
                print("Invalid shop name") # If left blank, this error message will appear
        elif choice == "2":
            display_shops()
            shop_index = select_shop()
            new_location = input("Enter new shop location: ")
            if Shopname[shop_index].change_shop_location(new_location):
                print("Shop location changed successfully!")
            else:
                print("Invalid shop location")
        elif choice == "3":
            display_shops()
            print()
            shop_index = select_shop()
            Shopname[shop_index].display_shop()
        elif choice == "4":
            for shop in Shopname:
                shop.display_shop()
                print(f"Customers: {shop.customers}")
                print(f"Sales: {shop.sales}")
                print(f"Returns: {shop.returns}\n")
        elif choice == "0":
            break
        else:
            print("Invalid option")


def display_shops():
    for i, shop in enumerate(Shopname):
        print(f"{i+1}. {shop.shopName}")


def select_shop():
    while True:
        choice = input("Select a shop: ")
        try:
            shop_index = int(choice) - 1
            if 0 <= shop_index < len(Shopname):
                return shop_index
        except ValueError:
            pass
        print("Invalid shop choice")


def option2():
    while True:
        print("Available items to sell:")
        for i, (item, details) in enumerate(ctuStock.stock.items()):
            print(f"{i+1}. {item} (R{details[0]:.2f})")

        try:
            item_index = int(input("Select an item to sell: ")) - 1
            if 0 <= item_index < len(ctuStock.stock):
                quantity = int(input("Enter quantity to sell: "))
                display_shops()
                shop_index = select_shop()
                success, message = Shopname[shop_index].sell_item(
                    list(ctuStock.stock.keys())[item_index], quantity
                )
                if success:
                    print("Sale successful!")
                    print(message)
                else:
                    print("Sale unsuccessful:", message)
        except ValueError:
            print("Invalid input")


def option3():
    while True:
        item = input("Enter item to return: ")
        quantity = int(input("Enter quantity to return: "))
        display_shops()
        shop_index = select_shop()
        success, message = Shopname[shop_index].return_item(item, quantity)
        if success:
            print("Return successful!")
            print(message)
        else:
            print("Return unsuccessful:", message)
        break


def option4():
    while True:
        print("1. Display stock")
        print("2. Add stock")
        print("0. Back")
        choice = input("Select an option: ")
        if choice == "1":
            ctuStock.display_stock()
        elif choice == "2":
            item = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter initial quantity: "))
            ctuStock.add_stock(item, price, quantity)
        elif choice == "0":
            break
        else:
            print("Invalid option")


opt_menus = True
while opt_menus != "99":
    main_menu()
    opt_menus = input("Select an option or 99 to exit: ")
    if opt_menus == "1":
        option1()
    elif opt_menus == "2":
        option2()
    elif opt_menus == "3":
        option3()
    elif opt_menus == "4":
        option4()
    elif opt_menus != "99":
        print("Invalid option")
>>>>>>> origin/main
