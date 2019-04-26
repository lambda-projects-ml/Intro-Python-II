# Write a class to hold player information, e.g. what room they are in
# currently.
from inventory import Inventory


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.health = 100
        self.sheild = 10
        self.carryWeight = 10

# Move player
    def move(self, new_room):
        new_room = new_room.lower()

        if new_room == 'n':
            if self.current_room.n_to == 'none':
                print("No room that directions \n\n")
            else:
                self.current_room = self.current_room.n_to
        elif new_room == 's':
            if self.current_room.s_to == 'none':
                print("No room that directions \n\n")
            else:
                self.current_room = self.current_room.s_to
        elif new_room == 'e':
            if self.current_room.e_to == 'none':
                print("No room that directions \n\n")
            else:
                self.current_room = self.current_room.e_to
        elif new_room == 'w':
            if self.current_room.w_to == 'none':
                print("No room that directions \n\n")
            else:
                self.current_room = self.current_room.w_to


# Check Inventory

    def check_inventory(self):
        print("Inventory:")
        for i in self.inventory:
            print(
                f'  Name:{i.name} \n  Description: {i.description} \n  Weight: {i.weight} \n')

# Check player status
    def check_status(self):
        print("Player Stats:")
        print(f'  Name: {self.name} \n  Room: {self.current_room.name} \n  Health: {self.health} \n  Sheild: {self.sheild} \n  Carry Weight: {self.carryWeight}')

# Check for items in the room
    def check_for_items(self):
        print('Items in the room:')
        for i in self.current_room.items:
            print(f'  {i.name}')

# Add item to inventory
    def add_to_inventory(self, item):
        self.inventory.append(item)

# Pickup item
    def pickup_item(self, item):
        x = 0
        if len(self.current_room.items) == 0:
            print("No items to pickup")
        else:
            for i in self.current_room.items:
                if i.name.capitalize() == item.capitalize():
                    weight = self.carryWeight - int(i.weight)
                    if weight >= 0:
                        self.carryWeight -= int(i.weight)
                        self.inventory.append(i)
                        self.current_room.items.remove(i)
                        x = 1
                        print(f'You picked up a {i.name}')
                    else:
                        x = 2

            if x == 0:
                print(f'\n\nThe item {item} is not in the room. \n\n')
            elif x == 2:
                print(
                    f'Unable to carry {i.name}, not enought carry weight available. Please drop another item first.')

    def drop_item(self, item):
        x = 0
        if len(self.inventory) == 0:
            print("No items to drop")
        else:
            for i in self.inventory:
                if i.name.capitalize() == item.capitalize():
                    self.inventory.remove(i)
                    self.current_room.items.append(i)
                    self.carryWeight += int(i.weight)
                    print(f'You dropped a {i.name}\n')
                    x = 1

            if x == 0:
                print("Item not in invetory")

    def __str__(self):
        return f'Player: {self.name}  {self.current_room}'
