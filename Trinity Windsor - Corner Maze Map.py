corner_maze_map = {
    'PUPPYCORNER': {
        'NAME': "Puppy Corner",
        'DESCRIPTION': "You are in a room full of Corgie puppies. One puppy gaurds a locked trap door, "
                       "south and east are open doors.",
        'PATHS': {
            'SOUTH': 'FROYOROOM',
            'EAST': 'TWILIGHTLIBRARY',
            'NORTHEAST': 'LLAMACORNER',
            'SOUTHWEST': 'KOALACORNER',
        }
    },
    'FROYOROOM': {
        'NAME': "Froyo Room",
        'DESCRIPTION': "There is a bar of goodies for froyo. South is a hallway, north and east is a doorway.",
        'PATHS': {
            'SOUTH': 'HALLWAY1',
            'NORTH': 'PUPPYCORNER',
            'EAST': 'TWILIGHTLIBRARY',
        }
    },
    'HALLWAY1': {
        'NAME': "Hallway Number 1",
        'DESCRIPTION': "It is a short hallway, to the north, east, and south are doors.",
        'PATHS': {
            'NORTH': 'FROYOROOM',
            'EAST': 'BEANBAGROOM',
            'SOUTH': 'TVROOM'
        }
    },
    'TVROOM': {
        'NAME': "TV Room",
        'DESCRIPTION': "T.V's surround the room playing all different shows and movies. North is a hallway, "
                       "east and south are doors",
        'PATHS': {
            'NORTH': 'HALLWAY1',
            'EAST': 'SNACKROOM',
            'SOUTH': 'WATERSLIDEROOM',
        }
    },
    'WATERSLIDEROOM': {
        'NAME': "Waterslide Room",
        'DESCRIPTION': "Water fills the room with fun slides. North and south are doors.",
        'PATHS': {
            'NORTH': 'TVROOM',
            'SOUTH': 'FLOWERROOM',
        }
    },
    'FLOWERROOM': {
        'NAME': "Flower Room",
        'DESCRIPTION': "Beautiful flowers and scents around are around the room. North and east is a door, "
                       "and south is a door with strange noises behind it",
        'PATHS': {
            'EAST': 'GARDENROOM',
            'SOUTH': 'KOALACORNER',
            'NORTH': 'WATERSLIDEROOM',
        }
    },
    'KOALACORNER': {
        'NAME': "Koala Corner",
        'DESCRIPTION': "Koalas fill the room, one koala plays with what looks like something you may need. "
                       "There are doors north and east",
        'PATHS': {
            'NORTH': 'FLOWERROOM',
            'EAST': 'GARDEN',
        }
    },
    'TWILIGHTLIBRARY': {
        'NAME': "Twilight Library",
        'DESCRIPTION': "The library is full of all the different genres of books, most book are the Twilight series."
                       " There are doors north, south, east, and west.",
        'PATHS': {
            'NORTH': 'PUPPYCORNER',
            'SOUTH': 'BEANBAGROOM',
            'EAST': 'COMPUTERROOM',
            'WEST': 'FROYOROOM',
        }
    },
    'BEANBAGROOM': {
        'NAME': "Bean Bag Room",
        'DESCRIPTION': "The room is filled with soft chairs and tables. West is a hallway, north, east and south "
                       "are doors.",
        'PATHS': {
            'WEST': 'HALLWAY1',
            'NORTH': 'TWILIGHTLIBRARY',
            'EAST': 'GYM',
            'SOUTH': 'BATHROOM1',
        }
    },
    'BATHROOM1': {
        'NAME': "Bathroom1",
        'DESCRIPTION': "There is a toilet, sink, and shower. There are two doors, one east, and one west.",
        'PATHS': {
            'EAST': 'GYM',
            'WEST': 'BEANBAGROOM',
        }
    },
    'GARDENROOM': {
        'NAME': "Garden Room",
        'DESCRIPTION': "The room is full with all sorts of different plants. There are doors south, east, and west. "
                       "Souths door has noises behind it.",
        'PATHS': {
            'SOUTH': 'KOALACORNER',
            'EAST': 'TEDDYROOM',
            'WEST': 'FLOWERROOM',
        }
    },
    'COMPUTERROOM': {
        'NAME': "Computer Room",
        'DESCRIPTION': "Computers on desks are all around the room for gaming. There are doors north, south, and west. "
                       "East is a hallway.",
        'PATH': {
            'NORTH': 'BALLPITROOM',
            'SOUTH': 'GYM',
            'EAST': 'HALLWAY2',
            'WEST': 'TWILIGHTLIBRARY',
        }
    },
    'GYM': {
        'NAME': "Gym",
        'DESCRIPTION': "The room is full of equipment, weights, and yogo mats. There are doors north, south, east,"
                       " and west",
        'PATHS': {
            'NORTH': 'COMPUTERROOM',
            'SOUTH': 'BATHROOM1',
            'EAST': 'PANDAEXPRESS',
            'WEST': 'BEANBAGROOM',
        }
    },
    'SNACKROOM': {
        'NAME': "Snack Room",
        'DESCRIPTION': "The room is full of sweets and drinks. There are doors south, east, and west.",
        'PATHS': {
            'SOUTH': 'TEDDYROOM',
            'EAST': 'PARTYROOM',
            'WEST': 'TVROOM',
        }
    },
    'TEDDYROOM': {
        'NAME': "Teddy Room",
        'DESCRIPTION': "The room gives off a happy and comforting vibe with all te teddys filling the room. "
                       "There are doors north, west, and south. South there is a staircase leading down.",
        'PATHS': {
            'NORTH': 'SNACKROOM',
            'SOUTH': 'LOSWERLAYER',
            'EAST': 'POSTERROOM',
            'WEST': 'GARDEN',
        }
    },
   'LOSERLAYER':{
       'NAME': "Loser Layer",
       'DESCRIPTION': "The layer is full of posters, empty soda cans, and ripped punching bags.There is a door to the "
                      "east and there are three staircases leading up, choose  UP1, UP2, or UP3.",
       'PATHS': {
            'UP1': 'TEDDYROOM',
            'UP2': 'POSTERROOM',
            'UP3': 'MONEYROOM',
        }
   },
    'HALLWAY2':{
        'NAME': "Hallway number 3",
        'DESCRIPTION': "The hallway gets louder at the door to the east. There are doors west, and south.",
        'PATHS': {
            'EAST': 'PARTYROOM',
            'WEST': 'COMPUTERROOM',
            'SOUTH': 'PANDAEXPRESS',
        }
    },
    'PANDAEXPRESS':{
        'NAME': "Panda Express",
        'DESCRIPTION': "There is a serve yourself food bar with tables and chairs to eat. North is a hallway, north "
                       "is a door with lights behind it, and east and west there are doors.",

    }
}

current_node = corner_maze_map['PUPPYCORNER']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'EASTWEST', 'NORTHEAST', 'NORTHWEST', 'SOUTHWEST', 'SOUTHEAST',
              'UP1', 'UP2', 'UP3']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = corner_maze_map[name_of_node]
        except KeyError:
            print("You cannot go this way.")
    else:
        print("Command not recognized")
        print()
