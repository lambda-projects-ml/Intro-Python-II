from player import Player
from item import Item


class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f'Room:\n  Location: {self.name.capitalize()} \n  Description: {self.description}'
