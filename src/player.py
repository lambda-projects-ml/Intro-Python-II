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

    # def change_room(self, new_room):
    #     print(f'{self.current_room}, {new_room}')

    def check_inventory(self):
        print("Inventory:")
        for i in self.inventory:
            print(i)

    def check_status(self):
        print("Player Stats:")
        print(f'  Name: {self.name} \n  Room: {self.current_room.name} \n  Health: {self.health} \n  Sheild: {self.sheild} \n  Carry Weight: {self.carryWeight}')

    def check_for_items(self):
        print('Items in the room:')
        for i in self.current_room.items:
            print(f'  {i}')

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def __str__(self):
        return f'Player: {self.name}  {self.current_room}'
