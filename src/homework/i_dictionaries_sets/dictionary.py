#
def add_inventory(inventory, item, quantity):

    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity


def remove_inventory_widget(inventory, item):

    if item in inventory:
        del inventory[item]