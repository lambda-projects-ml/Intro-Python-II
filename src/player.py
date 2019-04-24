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

    def move(self, new_room):
        if new_room == 'N':
            self.current_room = self.current_room.n_to
        elif new_room == 'S':
            self.current_room = self.current_room.s_to
        elif new_room == 'E':
            self.current_room = self.current_room.e_to
        elif new_room == 'W':
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
        if item in self.current_room.items:
            self.inventory.append(item)
        else:
            print('Item not in the room')

    def __str__(self):
        return f'Player: {self.name}  {self.current_room}'
