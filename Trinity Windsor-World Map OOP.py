class Room(object):
    def __init__(self, name, north, south, east, west, northeast, northwest, southwest, southeast, up1, up2,
                 up3, description):
        self.name = name
        self.description = description
        self.west = west
        self.east = east
        self.south = south
        self.north = north
        self.northeast = northeast
        self.northwest = northwest
        self.southwest = southwest
        self.southeast = southeast
        self.up1 = up1
        self.up2 = up2
        self.up3 = up3

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
Puppy_Corner = Room("Puppy Corner", None, "Froyo_Room", "Twilight_Library", None, "Llama_Corner", None, "Koala_Corner",
                    None, None, None, None, "You are in a room full of Corgie puppies. One puppy gaurds a locked"
                    " trap door, south and east are open doors.")
Froyo_Room = Room("Froyo Room", "Puppy_Corner", "Hallway1", "Twilight_Library", None, None, None, None, None, None,
                  None, None, "There is a bar of goodies for froyo. South is a hallway, north and east is a doorway.")
Hallway1 = Room("Hallway1", "Froyo_Room", "TV_Room", "Bean_Bag_Room", None, None, None, None, None, None, None, None,
                "It is a short hallway, to the north, east, and south are doors.")
TV_Room = Room("TV Room", "Hallway1", "Water_Slide_Room", "Snack_Room", None, None, None, None, None, None, None, None,
               "T.V's surround the room playing all different shows and movies. North is a hallway, east and south "
               "are doors")
Water_Slide_Room = Room("Water Slide Room", "TV_Room", "Flower_Room", None, None, None, None, None, None, None, None,
                        None, "Water fills the room with fun slides. North and south are doors.")
Flower_Room = Room("Flower Room", "Water_Slide_Room", "Koala_Corner", "Garden_Room", None, None, None, None, None,
                   None, None, None, "Beautiful flowers and scents around are around the room. North and east is a"
                   "door, and south is a door with strange noises behind it")
Koala_Corner = Room("Koala Corner", "Flower_Room", None, "Garden_Room", None, None, "Puppy_Corner", None,
                    "Penguin_Corner", None, None, None,  "Koalas fill the room, one koala plays with what looks like"
                    " something you may need. There are doors north and east")
Twilight_Library = Room("Twilight Library", "Puppy_Corner", "Bean_Bag_Room", "Computer_Room", "Froyo_Room", None, None,
                        None, None, None, None, None, "The library is full of all the different genres of books, most "
                        "book are the Twilight series.There are doors north, south, east, and west.")
Bean_Bag_Room = Room("Bean Bag Room", "Twilight_Library", "Bathroom1", "Gym", "Hallway1", None, None, None, None, None,
                     None, None, "The room is filled with soft chairs and tables. West is a hallway, north, east and "
                     "south are doors.")
Bathroom1 = Room("Bathroom1", None, None, "Gym", "Bean_Bag_Room", None, None, None, None, None, None, None, "There is"
                 " a toilet, sink, and shower. There are two doors, one east, and one west.")
Garden_Room = Room("Garden Room", None, "Koala_Corner", "Teddy_Room", "Flower_Room", None, None, None, None, None,
                   None, None, "The room is full with all sorts of different plants. There are doors south, east, "
                   "and west. Souths door has noises behind it.")
Computer_Room = Room("Computer Room", "Ball_Pit_Room", "Gym", "Hallway2", "Twilight_Library", None, None, None, None,
                     None, None, None, "Computers on desks are all around the room for gaming. There are doors north,"
                     " south, and west. East is a hallway.")
Gym = Room("Gym", "Computer_Room", "Bathroom1", "Panda_Express", "Bean_Bag_Room", None, None, None, None, None, None,
           None, "The room is full of equipment, weights, and yogo mats. There are doors north, south, east, and west")
Snack_Room = Room("Snack Room", None, "Teddy_Room", "Party_Room", "TV_Room", None, None, None, None, None, None, None,
                  "The room is full of sweets and drinks. There are doors south, east, and west.")
Teddy_Room = Room("Teddy Room", "Snack_Room", "Loser_Layer", "Poster_Room", "Garden Room", None, None, None, None,
                  None, None, None, "The room gives off a happy and comforting vibe with all te teddys filling the"
                  " room. There are doors north, west, and south. South there is a staircase leading down.")
Loser_Layer = Room("Loser Layer", None, "Pengiun_Corner", None, None, None, None, None, None, "Teddy_Room",
                   "Poster_Room", "Money_Room", "The layer is full of posters, empty soda cans, and ripped punching "
                   "bags.There is a door to the east and there are three staircases leading up, choose  UP1, UP2, or "
                   "UP3.")
Hallway2 = Room("Hallway2", None, "Panda_Express", "Party_Room", "Computer_Room", None, None, None, None, None, None,
                None, "The hallway gets louder at the door to the east. There are doors west, and south.")
Panda_Express = Room("Panda Express", "Hallway2", "Go_Cart_Racing_Room", "Party_Room", "Gym", None, None, None, None,
                     None, None, None, "There is a serve yourself food bar with tables and chairs to eat. North is a "
                     "hallway, north is a door with lights behind it, and east and west there are doors.")
Go_Cart_Racing_Room = Room("Go Cart Racing Room", "Panda_Express", None, "Party_Room", None, None, None, None, None,
                           None, None, None, "Go cart tracks circle the room. There are doors east and north.")
Poster_Room = Room("Poster Room", "Party_Room", "Loser_Layer", "Money_Room", "Teddy_Room", None, None, None, None,
                   None, None, None, "All kinds of posters from different movies and games surround the walls. There "
                   "are doors north, east, and west. There is a staircase leading down to the south")
Money_Room = Room("Money Room", "Party_Room", "Loser_Layer", "Penguin_Corner", "Poster_Room", None, None, None, None,
                  None, None, None, "There is a pool of coins and money. North, east, and west are doors. South is a"
                  " staircase leading down.")
Party_Room = Room("Party Room", "Ball_Pit_Room", "Loser_Layer", "Movie_Room", "Panda_Express", None, None, None, None,
                  None, None, None, "Loud music, lights, and drinks are in the room. There are doors north, south,"
                  " east, and west.")
Ball_Pit_Room = Room("Ball Pit Room", None, "Party_Room", "Hallway3", "Computer_Room", None, None, None, None, None,
                     None, None, "Ball pits are all around the room. South and west are rooms, east is a hallway.")
Hallway3 = Room("Hallway3", None, "Party_Room", "Nail_Salon", "Ball_Pit_Room", None, None, None, None, None, None,
                None, "There are doors south, east, and west.")
Nail_Salon = Room("Nail Salon", None, "Movie_Room", "Llama_Corner", "Hallway3", None, None, None, None, None, None,
                  None, "Nail paints are on shelves against the walls, tables and chairs are all around the room. East"
                  " and south are doors and west is a hallway.")
Movie_Room = Room("Movie Room", "Nail_Salon", "Party_Room", "Llama_Corner", "Shoe_Closet", None, None, None, None,
                  None, None, None, "There is a projecter and there are reclining seats. There are doors north, south,"
                  " east, and west.")
Shoe_Closet = Room("Shoe Closet", "Movie_Room", "Laundry_Room", "Clothes_Closet", "Party_Room", None, None, None, None,
                   None, None, None, "All types of shoes fill the room. North, south, east, and west are rooms.")
Clothes_Closet = Room("Clothes Closet", None, "Mirror_Room", "Bathroom2", "Shoe_Closet", None, None, None, None, None,
                      None, None, "The room is full of extra clothes. There are doors west, east, and south.")
Laundry_Room = Room("Laundry Room", "Shoe_Closet", None, None, "Party_Room", None, None, None, None, None, None, None,
                    "The Room is full of washers and dryers. There are doors to the west and east.")
Mirror_Room = Room("Mirror Room", "Clothes_Closet", None, "Sushi_Room", None, None, None, None, None, None, None, None,
                   "The Room is full if different mirrors. There are doors north and east.")
Llama_Corner = Room("Llama Corner", None, "Bathroom2", "Party_Room", "Nail_Salon", None, "Puppy_Corner", "Movie_Room",
                    None, None, None, None, "The room is full of spit and llamas. One llama is stepping over an object"
                    " that could be of your use. There are doors south, east, and west.")
Bathroom2 = Room("Bathroom2", "Llama_Corner", None, None, "Clothes_Closet", None, None, None, None, None, None, None,
                 "Its a clean bathroom with shower access. There are doors north and west.")
Sushi_Room = Room("Sushi Room", "Party_Room", "Penguin_Corner", None, "Mirror_Room", None, None, None, None, None, None,
                  None, "The room is filled with a fish odor and barstools for eaating. There are doors north, south,"
                  " and west.")
Penguin_Corner = Room("Penguin Corner", "Sushi_Room", None, "Money_Room", "Loser_layer", None, None, "Koala_Corner",
                      None, None, None, None, "The room is filled with snow and penguins. One penguin carries something"
                      " between its legs. There are doors north, east, and west")


current_node = Puppy_Corner
directions = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southwest', 'southeast', 'up1', 'up2', 'up3']
short_direction = ['n', 's', 'e', 'w', 'ne', 'nw', 'sw', 'se', 'u1', 'u2', 'u3']
while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
    else:
        print("Command not recognized")
        print()
