class Item(object):
    def __init__(self, name):
        self.name = name

    def drop(self):
        print("You dropped the item")

    def put_away(self):
        print("you put away %s" % self.name)


class Wearable(Item):
    def __init__(self, name, wear):
        super(Wearable, self).__init__(name)
        self.wear = wear

    def put_on(self):
        print("You put it on")


class Clothes(Wearable):
    def __init__(self, name):
        super(Clothes, self).__init__(name, True)

    def wash(self):
        print("You washed your clothes")


class Hat(Clothes):
    def __init__(self):
        super(Hat, self).__init__("hat")

    def tip(self):
        print("you tipped your hat")


class Shirts(Clothes):
    def __init__(self):
        super(Shirts, self).__init__("shirt")

    def rip(self):
        print("you ripped your shirt in half like the movies")


class Pants(Clothes):
    def __init__(self):
        super(Pants, self).__init__("pants")

    def cuff(self):
        print("you cuffed the bottom of your pants")


class Shoes(Clothes):
    def __init__(self):
        super(Shoes, self).__init__("shoes")

    def shine(self):
        print("you shine your shoes")


class Accessories(Wearable):
    def __init__(self, name):
        super(Accessories, self).__init__(name, True)

    def polish(self):
        print("you polish %s" % self.name)


class Pouch(Accessories):
    def __init__(self):
        super(Pouch, self).__init__("pouch")

    def open(self):
        print("you opened the pouch")


class Backpack(Accessories):
    def __init__(self):
        super(Backpack, self).__init__("backpack")

    def burn(self):
        print("the backpack catches on fire")


class Jewelry(Accessories):
    def __init__(self, name, money):
        super(Jewelry, self).__init__(name)
        self.money = money

    def sell(self):
        print("you sold it for %s" % self.money)


class Necklaces(Jewelry):
    def __init__(self):
        super(Necklaces, self).__init__("necklace", 100)

    def borrow(self):
        print("you borrow it")


class Bracelets(Jewelry):
    def __init__(self):
        super(Bracelets, self).__init__("bracelet", 50)

    def carve_name(self):
        print("you carve your name into the bracelet")


class Consumable(Item):
    def __init__(self, name, eat):
        super(Consumable, self).__init__(name)
        self.eat = eat

    def consume(self):
        print("You ate the item")


class Food(Consumable):
    def __init__(self, name, eat):
        super(Food, self).__init__(name, eat)

    def cook(self):
        print("you cooked %s" % self.name)


class Froyo(Food):
    def __init__(self):
        super(Froyo, self).__init__("frozen yogurt", True)

    def lick(self):
        print("you lick your froyo")


class Sushi(Food):
    def __init__(self):
        super(Sushi, self).__init__("Sushi", True)

    def barf(self):
        print("you barf because sushi is gross")


class Candy(Food):
    def __init__(self):
        super(Candy, self).__init__("candy", True)

    def sugar_rush(self):
        print("you are bouncing off the walls. It would be a smart idea to take a nap")


class Popcorn(Food):
    def __init__(self):
        super(Popcorn, self).__init__("Popcorn", True)

    def shove(self):
        print("you shove your mouth full of popcorn")


class Grilled_Chicken(Food):
    def __init__(self):
        super(Grilled_Chicken, self).__init__("Grilled chicken", True)

    def cut(self):
        print("you cut your chicken")


class Snacks(Food):
    def __init__(self):
        super(Snacks, self).__init__("random snacks", True)

    def take(self):
        print("you take as many snacks as you can")


class Drinks(Consumable):
    def __init__(self, name):
        super(Drinks, self).__init__(name, False)
        self.full = True

    def drink(self):
        print("You drank it")
        self.full = False


class Water(Drinks):
    def __init__(self):
        super(Water, self).__init__("water")

    def hydrate(self):
        print("your body is hydrated")


class Soda(Drinks):
    def __init__(self):
        super(Soda, self).__init__("soda")

    def burp(self):
        print("you burped super loud")


class Beer(Drinks):
    def __init__(self):
        super(Beer, self).__init__("beer")

    def drunk(self):
        print("your drunk and ran into a wall")


class Weapon(Item):
    def __init__(self, name, attack_damage):
        super(Weapon, self).__init__(name)
        self.durability = 100
        self.attack_damage = attack_damage

    def attack(self):
        print("You attacked")
        self.durability -= 5
        print(self.durability)

    def throw(self):
        print("You throw the %s" % self.name)


class Stick(Weapon):
    def __init__(self):
        super(Stick, self).__init__("stick", 5)

    def poke(self):
        print("nothing happened")


class Spoon(Weapon):
    def __init__(self):
        super(Spoon, self).__init__("spoon", 5)

    def throw(self):
        super(Spoon, self).throw()
        print("It isn't very effective...")


class Book(Weapon):
    def __init__(self):
        super(Book, self).__init__("book", 5)

    def read(self):
        print("you read the book")


class Flower(Item):
    def __init__(self):
        super(Flower, self).__init__("flower")

    def smell(self):
        print("You smell the flower")


class Money(Item):
    def __init__(self):
        super(Money, self).__init__("Money")

    def rain(self):
        print("you made it rain money. a coin hit your eye")


class Key(Item):
    def __init__(self, name):
        super(Key, self).__init__(name)

    def open(self):
        print("you open using the key")


class TV(Item):
    def __init__(self):
        super(TV, self).__init__("TV")

    def watch(self):
        print("your watching tv")

    def change_channel(self):
        print("you change the channel")


class Character(object):
    def __init__(self, name, attack, description, status):
        self.name = name
        self.attack_amt = attack
        self.description = description
        self.status = status
        self.health = 100
        self.inventory = []

    def attack(self, target):
        target.damage(self.attack_amt)

    def damage(self, dmg):
        self.health -= dmg


class Water_Slide(Item):
    def __init__(self):
        super(Water_Slide, self).__init__("water slide")

    def slide(self):
        print("you slide down the waterslide")


class Bamboo(Consumable):
    def __init__(self):
        super(Bamboo, self).__init__("Bamboo", True)

    def feed(self):
        print("You fed it to %s" % self.name)


class Bean_Bag(Item):
    def __init__(self):
        super(Bean_Bag, self).__init__("bean bag")

    def sit(self):
        print("You sat comfortably in the bean bag")


class Towel(Item):
    def __init__(self):
        super(Towel, self).__init__("Towel")

    def dry(self):
        print("you dry it")


class Plants(Item):
    def __init__(self):
        super(Plants, self).__init__("Plants")

    def pick(self):
        print("you pick the plants")


class Computer(Item):
    def __init__(self):
        super(Computer, self).__init__("Computer")

    def play(self):
        print("you play on the computer")


class Treadmill(Item):
    def __init__(self):
        super(Treadmill, self).__init__("treadmill")

    def run(self):
        print("you started to run on the treadmill")


class Teddy(Item):
    def __init__(self):
        super(Teddy, self).__init__("Teddy bear")

    def cuddle(self):
        print("you cuddle with a bear")


class Go_Cart(Item):
    def __init__(self):
        super(Go_Cart, self).__init__("go cart")

    def drive(self):
        print("you drive the go cart")


class Poster(Item):
    def __init__(self):
        super(Poster, self).__init__("poster")

    def hang(self):
        print("you hang the poster")


class Ball(Item):
    def __init__(self):
        super(Ball, self).__init__("ball")

    def throw(self):
        print("You threw the ball")


class Nail_Polish(Item):
    def __init__(self):
        super(Nail_Polish, self).__init__("nail polish")

    def color(self, color):
        self.color = color
        print("you chose %s" % self.color)


class Mirror(Item):
    def __init__(self):
        super(Mirror, self).__init__("mirror")

    def pose(self):
        print("you pose in the mirror")


puppy = Character("puppy", 3, "It's a crazy little puppy.", "rambunctious")
koala = Character("koala", 4, "It's a cute little koala", "lazy")
penguin = Character("penguin", 6, "It's a hungry penguin", "pissed")
llama = Character("llama", 5, "It's a stinky llama", "tired")
you = Character("you", 20, "It's you", None)
panda = Character("panda", None, "Its a serving panda", "working")
puppy_god = Character("puppy god", 50, "PUPPYYYYY GOOOODDDD", "ANGRY")


class Room(object):
    def __init__(self, name, north, south, east, west, northeast, northwest, southwest, southeast, up1, up2,
                 up3, description, characters, item):
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
        self.characters = characters
        self.item = item

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


froyo = Froyo()
spoon = Spoon()
water = Water()
soda = Soda()
candy = Candy()
tv = TV()
water_slide = Water_Slide()
flower = Flower()
bamboo = Bamboo()
book = Book()
bean_bag = Bean_Bag()
towel = Towel()
plants = Plants()
stick = Stick()
computer = Computer()
treadmill = Treadmill()
snacks = Snacks()
teddy = Teddy()
beer = Beer()
grilled_chicken = Grilled_Chicken()
go_cart = Go_Cart()
money = Money()
key = Key("key")
ball = Ball()
nail_polish = Nail_Polish()
popcorn = Popcorn()
shoes = Shoes()
shirts = Shirts()
pants = Pants()
hat = Hat()
necklaces = Necklaces()
bracelets = Bracelets()
backpack = Backpack()
pouch = Pouch()
clothes = Clothes("clothes")
mirror = Mirror()
sushi = Sushi()

Puppy_Corner = Room("Puppy Corner", None, "Froyo_Room", "Twilight_Library", None, "Llama_Corner", None, "Koala_Corner",
                    None, None, None, None, "You are in a room full of Corgie puppies. One puppy gaurds a locked"
                    " trap door, south and east are open doors.", puppy, None)
Trap_Door = Room("Trap Door", None, None, None, None, None, None, None, None, None, None, None, "You have entered into "
                 "the trap door and came face to face with the puppy god", puppy_god, None)
Froyo_Room = Room("Froyo Room", "Puppy_Corner", "Hallway1", "Twilight_Library", None, None, None, None, None, None,
                  None, None, "There is a bar of goodies for froyo. South is a hallway, north and east is a doorway.",
                  None, [froyo, spoon, water, soda, candy])
Hallway1 = Room("Hallway1", "Froyo_Room", "TV_Room", "Bean_Bag_Room", None, None, None, None, None, None, None, None,
                "It is a short hallway, to the north, east, and south are doors.", None, None)
TV_Room = Room("TV Room", "Hallway1", "Water_Slide_Room", "Snack_Room", None, None, None, None, None, None, None, None,
               "T.V's surround the room playing all different shows and movies. North is a hallway, east and south "
               "are doors", None, [tv, soda])
Water_Slide_Room = Room("Water Slide Room", "TV_Room", "Flower_Room", None, None, None, None, None, None, None, None,
                        None, "Water fills the room with fun slides. North and south are doors.", None, [water_slide,
                        water])
Flower_Room = Room("Flower Room", "Water_Slide_Room", "Koala_Corner", "Garden_Room", None, None, None, None, None,
                   None, None, None, "Beautiful flowers and scents around are around the room. North and east is a"
                   "door, and south is a door with strange noises behind it", None, [flower])
Koala_Corner = Room("Koala Corner", "Flower_Room", None, "Garden_Room", None, None, "Puppy_Corner", None,
                    "Penguin_Corner", None, None, None,  "Koalas fill the room, one koala plays with what looks like"
                    " something you may need. There are doors north and east", koala, [bamboo, Key])
Twilight_Library = Room("Twilight Library", "Puppy_Corner", "Bean_Bag_Room", "Computer_Room", "Froyo_Room", None, None,
                        None, None, None, None, None, "The library is full of all the different genres of books, most "
                        "book are the Twilight series.There are doors north, south, east, and west.", None, [book])
Bean_Bag_Room = Room("Bean Bag Room", "Twilight_Library", "Bathroom1", "Gym", "Hallway1", None, None, None, None, None,
                     None, None, "The room is filled with soft chairs and tables. West is a hallway, north, east and "
                     "south are doors.", None, [bean_bag])
Bathroom1 = Room("Bathroom1", None, None, "Gym", "Bean_Bag_Room", None, None, None, None, None, None, None, "There is"
                 " a toilet, sink, and shower. There are two doors, one east, and one west.", None, [towel])
Garden_Room = Room("Garden Room", None, "Koala_Corner", "Teddy_Room", "Flower_Room", None, None, None, None, None,
                   None, None, "The room is full with all sorts of different plants. There are doors south, east, "
                   "and west. Souths door has noises behind it.", None, [plants, stick])
Computer_Room = Room("Computer Room", "Ball_Pit_Room", "Gym", "Hallway2", "Twilight_Library", None, None, None, None,
                     None, None, None, "Computers on desks are all around the room for gaming. There are doors north,"
                     " south, and west. East is a hallway.", None, [computer])
Gym = Room("Gym", "Computer_Room", "Bathroom1", "Panda_Express", "Bean_Bag_Room", None, None, None, None, None, None,
           None, "The room is full of equipment, weights, and yogo mats. There are doors north, south, east, and west",
           None, [treadmill, water])
Snack_Room = Room("Snack Room", None, "Teddy_Room", "Party_Room", "TV_Room", None, None, None, None, None, None, None,
                  "The room is full of sweets and drinks. There are doors south, east, and west.", None,
                  [snacks, water, soda, candy])
Teddy_Room = Room("Teddy Room", "Snack_Room", "Loser_Layer", "Poster_Room", "Garden Room", None, None, None, None,
                  None, None, None, "The room gives off a happy and comforting vibe with all te teddys filling the"
                  " room. There are doors north, west, and south. South there is a staircase leading down.", None,
                  [teddy])
Loser_Layer = Room("Loser Layer", None, "Pengiun_Corner", None, None, None, None, None, None, "Teddy_Room",
                   "Poster_Room", "Money_Room", "The layer is full of posters, empty soda cans, and ripped punching "
                   "bags.There is a door to the east and there are three staircases leading up, choose  UP1, UP2, or "
                   "UP3.", None, [beer, soda])
Hallway2 = Room("Hallway2", None, "Panda_Express", "Party_Room", "Computer_Room", None, None, None, None, None, None,
                None, "The hallway gets louder at the door to the east. There are doors west, and south.", None,
                [towel])
Panda_Express = Room("Panda Express", "Hallway2", "Go_Cart_Racing_Room", "Party_Room", "Gym", None, None, None, None,
                     None, None, None, "There is a serve yourself food bar with tables and chairs to eat. North is a "
                     "hallway, north is a door with lights behind it, and east and west there are doors.", panda,
                     [water, grilled_chicken, soda])
Go_Cart_Racing_Room = Room("Go Cart Racing Room", "Panda_Express", None, "Party_Room", None, None, None, None, None,
                           None, None, None, "Go cart tracks circle the room. There are doors east and north.", None,
                           [go_cart])
Poster_Room = Room("Poster Room", "Party_Room", "Loser_Layer", "Money_Room", "Teddy_Room", None, None, None, None,
                   None, None, None, "All kinds of posters from different movies and games surround the walls. There "
                   "are doors north, east, and west. There is a staircase leading down to the south", None, [Poster])
Money_Room = Room("Money Room", "Party_Room", "Loser_Layer", "Penguin_Corner", "Poster_Room", None, None, None, None,
                  None, None, None, "There is a pool of coins and money. North, east, and west are doors. South is a"
                  " staircase leading down.", None, [money])
Party_Room = Room("Party Room", "Ball_Pit_Room", "Loser_Layer", "Movie_Room", "Panda_Express", None, None, None, None,
                  None, None, None, "Loud music, lights, and drinks are in the room. There are doors north, south,"
                  " east, and west.", None, [soda, water, beer, candy])
Ball_Pit_Room = Room("Ball Pit Room", None, "Party_Room", "Hallway3", "Computer_Room", None, None, None, None, None,
                     None, None, "Ball pits are all around the room. South and west are rooms, east is a hallway.",
                     None, [ball])
Hallway3 = Room("Hallway3", None, "Party_Room", "Nail_Salon", "Ball_Pit_Room", None, None, None, None, None, None,
                None, "There are doors south, east, and west.", None, None)
Nail_Salon = Room("Nail Salon", None, "Movie_Room", "Llama_Corner", "Hallway3", None, None, None, None, None, None,
                  None, "Nail paints are on shelves against the walls, tables and chairs are all around the room. East"
                  " and south are doors and west is a hallway.", None, [nail_polish])
Movie_Room = Room("Movie Room", "Nail_Salon", "Party_Room", "Llama_Corner", "Shoe_Closet", None, None, None, None,
                  None, None, None, "There is a projecter and there are reclining seats. There are doors north, south,"
                  " east, and west.", None, [popcorn, soda])
Shoe_Closet = Room("Shoe Closet", "Movie_Room", "Laundry_Room", "Clothes_Closet", "Party_Room", None, None, None, None,
                   None, None, None, "All types of shoes fill the room. North, south, east, and west are rooms.", None,
                   [shoes])
Clothes_Closet = Room("Clothes Closet", None, "Mirror_Room", "Bathroom2", "Shoe_Closet", None, None, None, None, None,
                      None, None, "The room is full of extra clothes. There are doors west, east, and south.", None,
                      [shirts, pants, hat, necklaces, bracelets, backpack, pouch])
Laundry_Room = Room("Laundry Room", "Shoe_Closet", None, None, "Party_Room", None, None, None, None, None, None, None,
                    "The Room is full of washers and dryers. There are doors to the west and east.", None, [clothes])
Mirror_Room = Room("Mirror Room", "Clothes_Closet", None, "Sushi_Room", None, None, None, None, None, None, None, None,
                   "The Room is full if different mirrors. There are doors north and east.", None, [mirror])
Llama_Corner = Room("Llama Corner", None, "Bathroom2", "Party_Room", "Nail_Salon", None, "Puppy_Corner", "Movie_Room",
                    None, None, None, None, "The room is full of spit and llamas. One llama is stepping over an object"
                    " that could be of your use. There are doors south, east, and west.", llama, [key])
Bathroom2 = Room("Bathroom2", "Llama_Corner", None, None, "Clothes_Closet", None, None, None, None, None, None, None,
                 "Its a clean bathroom with shower access. There are doors north and west.", None, [towel])
Sushi_Room = Room("Sushi Room", "Party_Room", "Penguin_Corner", None, "Mirror_Room", None, None, None, None, None, None,
                  None, "The room is filled with a fish odor and barstools for eating. There are doors north, south,"
                  " and west.", None, [sushi, water, soda])
Penguin_Corner = Room("Penguin Corner", "Sushi_Room", None, "Money_Room", "Loser_layer", None, None, "Koala_Corner",
                      None, None, None, None, "The room is filled with snow and penguins. One penguin carries something"
                      " between its legs. There are doors north, east, and west", penguin, [key])


current_node = Puppy_Corner
directions = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southwest', 'southeast', 'up1', 'up2', 'up3']
short_direction = ['n', 's', 'e', 'w', 'ne', 'nw', 'sw', 'se', 'u1', 'u2', 'u3']

while True:
    # print where you are
    print(current_node.name)
    print(current_node.description)
    print(current_node.characters.name)
    print()
    if current_node.item is None:
        print("There are no items in the room")
    if current_node.item is not None:
        print("There are the following items in the room:")
        for i,n in enumerate(current_node.item):
            print("%d : %s" %(i+1, n.name))
        print()


    # Takes in input
    command = input('>_').lower()

    if command == 'quit':
        quit(0)

    if command in short_direction:
        pos = short_direction.index(command)
        command = directions[pos]


    # Take Items
    if "take " in command:
        item_requested = command[5:]
        found = False
        for item in current_node.item:
            if item.name == item_requested:
                you.inventory.append(item)
                found = True
        if not found:
            print("I don't see it here")

    # Handles Movement
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
    else:
        print("Command not recognized")
        print()