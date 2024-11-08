#
from dictionary import add_inventory, remove_inventory_widget

def inventory_menu():

    print("\nInventory Menu")
    print("1- Add or Update Item")
    print("2- Delete Item")
    print("3- Exit")

def main():
    inventory = {}

    while True:
        inventory_menu()
        choice = input("Enter your selection: ")

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_inventory(inventory, item, quantity)
            print(f"Inventory updated: {inventory}")
        
        elif choice == '2':
            item = input("Enter item name for deletion: ")
            remove_inventory_widget(inventory, item)
            print(f"Inventory after deletion: {inventory}")
        
        elif choice == '3':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")
main()