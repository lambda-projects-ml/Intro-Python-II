from room import Room
from player import Player
from item import Item
import textwrap
import os


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

sword = Item('sword', 'Very big sword', '5')
bow = Item('bow', 'so fast', '3')

playerName = input("Your name: ")

# Make a new player object that is currently in the 'outside' room.
player = Player(playerName, current_room=room['outside'])
os.system('cls' if os.name == 'nt' else 'clear')
print(f'Welcome {player.name} \n_________________________________________')

# Print Testing
# print('---------------------\n')
# # Add items to rooom
# room['outside'].add_item(sword)
# room['outside'].add_item(bow)
# print(room['outside'])

# # Player Inventory
# player.add_to_inventory(sword)
# player.add_to_inventory(bow)
# player.check_inventory()

# # Player Status
# player.pickup_item('bow')
# player.check_status()

# # Check for items
# player.check_for_items()
# print(type(player.current_room.items[0]))


# print('---------------------\n')

# Write a loop that:

selection = str(
    input("[N] Move North  [S] Move South  [P] Pick Up Item  [Q] Quit\n"))
selection = selection.upper()
os.system('cls' if os.name == 'nt' else 'clear')

while not selection == 'Q':
    if selection == 'N':
        player.move(selection)
        print("Moved North")
        player.check_status()

    elif selection == 'S':
        player.move(selection)
        print("Moved South")
        player.check_status()

    elif selection == 'P':
        selection = str(input("Pickup item: "))
        player.pickup_item(selection)
        player.check_status()

    elif selection == 'Q':
        print('Goodbye')
        break

    else:
        print("Invalid selection")

    print('_________________________________________')
    selection = str(
        input("[N] Move North  [S] Move South  [P] Pick Up Item [Q] Quit\n"))
    selection = selection.upper()
    os.system('cls' if os.name == 'nt' else 'clear')


#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
