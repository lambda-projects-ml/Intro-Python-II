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
print('---------------------\n')

# Player Inventory
player.check_inventory()

# Player Status
player.check_status()

# Check for items
player.check_for_items()

# Add items to rooom
room['outside'].add_item(sword)
room['outside'].add_item(bow)
print(room['outside'])


print('---------------------\n')

# Write a loop that:

selection = str(input("[N] Move North  [S] Move South  [Q] Quit\n"))

while not selection == 'Q' or 'q':
    if selection == 'N' or 'n':
        print(selection)
        print("Moved North")
        print(player.check_status)
        print(player.current_room.description)

    elif selection == 'S' or 's':
        print("Moved South")
        print(player.current_room.name)
        print(player.current_room.description)

    else:
        print("Invalid selection")

    # os.system('cls' if os.name == 'nt' else 'clear')

    print('_________________________________________')
    selection = str(input("[N] Move North  [S] Move South  [Q] Quit\n"))
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
