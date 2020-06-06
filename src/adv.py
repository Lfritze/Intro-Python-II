import textwrap
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['Ninja-Sword', 'Bow-Staff']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['Beans', 'Gold-Nugget']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['Banana', 'Machete']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['Gold-Nugget', 'Ninja-Stars']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['Gold-Nugget', 'Tiger-Blood-Energy-Drink']),
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

# Make a new player object that is currently in the 'outside' room.
player = Player("Leighton", room['outside'])

done = False
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while not done:

    print('\n', player.location)

    print('\nItems in room ', player.location.items)

    print('\nItems in inventory ', player.items, '\n')

    for line in textwrap.wrap(player.location.print_description()):
        print('\n', line)
    print('\n')

    command = input(
        "What do you want to do?\nTo navigate use 'n' 's' 'e' 'w'\nTo pick up items use 'grab0', 'grab1', etc...\nTo drop items use 'drop0', 'drop1', etc...\n('q' or 'quit' to quit) ")

    if command in ['n', 's', 'e', 'w']:
        player.location = player.move_to(command, player.location)
        continue

    elif command[0] == 'grab':
        item = int(command[1:])
        if item >= 0 and item < len(player.location.items):
            print('\n', player.name, ' picks up ', player.location.items[item])
            player.add_item(player.location.items[item])
            player.location.remove_item(item)
        else:
            print('that item does not exist')

    elif command[0] == 'drop':
        item = int(command[1:])
        if item >= 0 and item < len(player.items):
            print('\n', player.name, ' drops ', player.items[item])
            player.location.add_item(player.items[item])
            player.remove_item(item)
        else:
            print('that item does not exist')

    elif command == 'q' or command == 'quit':
        done = True

    else:
        print('Invalid command you FOOL!, use n to move north, e to move east, s to move south, and w to move west \n')