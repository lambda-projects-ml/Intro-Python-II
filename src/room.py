from player import Player
from item import Item


class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = 'none'
        self.s_to = 'none'
        self.w_to = 'none'
        self.e_to = 'none'

    def add_item(self, item):
        self.items.append(item)
