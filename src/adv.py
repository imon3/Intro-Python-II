from room import Room
from player import Player
from item import Item

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

items = [
    ['bow', 'long bow'],
    ['sword', 'short sword'],
    ['mirror', 'magic mirror'],
    ['torch', 'fire']
]

item = [Item(item[0], item[1]) for item in items]

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].add_item(item)
room['foyer'].add_item(item)
room['overlook'].add_item(item)
room['narrow'].add_item(item)
room['treasure'].add_item(item)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Player 1', room['outside'])
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
print(
    'Enter a direction: [n] north, [e] east, [s] south, [w] west, or [q] to quit.\n')


directions = ['n', 'e', 's', 'w']


def get_room(way, current_room):
    if way == 'n':
        return current_room.n_to
    elif way == 'e':
        return current_room.e_to
    elif way == 's':
        return current_room.s_to
    elif way == 'w':
        return current_room.w_to


while True:
    print(player)
    print(player.current_room)
    # print(player.current_room.description)

    way = input(' -> ')

    if way in directions:
        new_room = get_room(way, player.current_room)
        print('Enter name of item to hold.\n')
        hold_item = input(' -> ')
        if new_room is not None:
            player.move_player(new_room)
            player.get_item(hold_item)
        else:
            print('Can not move in that direction')
    elif way == 'q':
        print('Thank you for playing.')
        break
    else:
        print('invalid key')
