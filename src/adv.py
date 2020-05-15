from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

# Create Items
gold_small = Money('Money - S', 'Small Pile of Gold', 15, 'Gold Coins')
gold_medium = Money('Money - M', 'Medium Pile of Gold', 50, 'Gold Coins')
gold_large = Money('Money - L', 'Large Pile of Gold', 100, 'Gold Coins')
print('!!! XXX !!!',gold_small)
print('!!! XXX !!!',gold_medium)
print('!!! XXX !!!',gold_large)

carrot = Food('Carrot', 'Crunchy and good for you', '14 pounds', 3)
taco_softShell = Food('Taco', 'FREE TACO OMG!!!!!!!!...oh its shoft shell...', '3 soft shell', 1000)
taco_hardShell = Food('Taco', 'FREE TACO OMG!!!!!!!!...AND ITS A REAL TACO SHELL', '3 hard shell', 5000)
print('!!! XXX !!!',carrot)
print('!!! XXX !!!',taco_softShell)
print('!!! XXX !!!',taco_hardShell)

# Add Items to Rooms
room['outside'].items = [gold_small, carrot]
room['foyer'].items = [carrot]
room['overlook'].items = [gold_large, taco_hardShell]
room['narrow'].items = [taco_softShell]
room['treasure'].items = [carrot]

#
# Main
#
# Directional Movements
movement = ['n','s','e','w']

# Make a new player object that is currently in the 'outside' room.

player = Player('Leighton', room['outside'])

# Write a loop that:
#
# * Prints the current room name
print(player.location)
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


