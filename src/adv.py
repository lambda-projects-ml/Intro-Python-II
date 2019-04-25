from room import Room
from player import Player
from item import Item
import textwrap
import random
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
earlier adventurers. The only exit is to the south.""")
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

# select random room
random = random.choice(list(room.keys()))

# Create Items
sword = Item('sword', 'Very big sword', '5')
bow = Item('bow', 'so fast', '6')
light = Item('light', 'much bright', '1')
key = Item('key', 'The one and only', '1')

# Assign items to room
room['outside'].add_item(sword)
room['outside'].add_item(bow)
room[random].add_item(key)


#
# Main
#
os.system('cls' if os.name == 'nt' else 'clear')
print('****** Adventure Game ****** \n')
playerName = input("Your name: ")

# Make a new player object that is currently in the 'outside' room.
player = Player(playerName, current_room=room['outside'])
os.system('cls' if os.name == 'nt' else 'clear')


# Parser
def Parser(selection):
    list = selection.split(' ')
    # Drop
    playerItems = player.inventory
    dropItem = ''
    for i in list:
        for x in playerItems:
            if i == x.name:
                dropItem = i
    # Get
    roomItems = player.current_room.items
    getItem = ''
    for i in list:
        for y in roomItems:
            if i == y.name:
                getItem = i

    # Logic
    if ("get" or "take") in list:
        player.pickup_item(getItem)
    elif "drop" in list:
        print('drop if')
        player.drop_item(dropItem)


print(
    f'****** Adventure Game ****** \n\nWelcome {player.name} \n\n_________________________________________')

# Write a loop that:
selection = str(input(
    "[N] Move North  [S] Move South  [E] Move East  [W] Move West  \n[A] Action  [I] Inventory  [P] Pick Up Item  [D] Drop Item  [Q] Quit\n-> ")).upper()

os.system('cls' if os.name == 'nt' else 'clear')

while not selection == 'Q':
    print('****** Adventure Game ****** \n')
    if selection == 'N':
        player.move(selection)
        player.check_status()

    elif selection == 'S':
        player.move(selection)
        player.check_status()

    elif selection == 'E':
        player.move(selection)
        player.check_status()

    elif selection == 'W':
        player.move(selection)
        player.check_status()

    elif selection == 'A':
        selection = str(input("What would you like to do?\n-> "))
        Parser(selection)
        player.check_status()
        print('\n')
        player.check_inventory()

    elif selection == 'P':
        selection = str(input("Pickup item: "))
        print('\n')
        player.pickup_item(selection)
        print('\n')
        player.check_status()
        print('\n')
        player.check_inventory()

    elif selection == 'I':
        player.check_status()
        print('\n')
        player.check_inventory()

    elif selection == 'D':
        selection = str(input("Which item would you like to drop?\n-> "))
        print('\n')
        player.drop_item(selection)

    elif selection == '.':
        player.check_for_items()

    elif selection == 'Q':
        break

    else:
        print("Invalid selection")

    print('_________________________________________')
    selection = str(
        input("[N] Move North  [S] Move South  [E] Move East  [W] Move West  \n[A] Action  [I] Inventory  [P] Pick Up Item  [D] Drop Item  [Q] Quit\n-> "))
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
