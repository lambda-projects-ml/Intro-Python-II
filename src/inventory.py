class Inventory:
    def __init__(self, items):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def print(self):
        for i in self.items:
            print(i)

    def __str__(self):
        return f'{self.items}'
