def print_room_info(room):
    print("You are in %s." % room.name)
    print(room.description)
    if room.characters is not None:
        print("There is a %s in the room." % room.characters.name)
    else:
        print("There are no characters in the room.")
    if room.item is None:
        print("There are no items in the room.")
    else:
        print("There are the following items in the room:")
        for i, n in enumerate(room.item):
            print("%d : %s" % (i + 1, n.name))
        print()


class Item(object):
    def __init__(self, name):
        self.name = name


class Wearable(Item):
    def __init__(self, name, wear):
        super(Wearable, self).__init__(name)
        self.wear = wear


class Clothes(Wearable):
    def __init__(self, name):
        super(Clothes, self).__init__(name, True)


class Hat(Clothes):
    def __init__(self):
        super(Hat, self).__init__("hat")


class Shirts(Clothes):
    def __init__(self):
        super(Shirts, self).__init__("shirt")


class Pants(Clothes):
    def __init__(self):
        super(Pants, self).__init__("pants")


class Shoes(Clothes):
    def __init__(self):
        super(Shoes, self).__init__("shoes")


class Accessories(Wearable):
    def __init__(self, name):
        super(Accessories, self).__init__(name, True)


class Pouch(Accessories):
    def __init__(self):
        super(Pouch, self).__init__("pouch")


class Backpack(Accessories):
    def __init__(self):
        super(Backpack, self).__init__("backpack")


class Jewelry(Accessories):
    def __init__(self, name, money):
        super(Jewelry, self).__init__(name)
        self.money = money


class Necklaces(Jewelry):
    def __init__(self):
        super(Necklaces, self).__init__("necklace", 100)


class Bracelets(Jewelry):
    def __init__(self):
        super(Bracelets, self).__init__("bracelet", 50)


class Consumable(Item):
    def __init__(self, name, eat):
        super(Consumable, self).__init__(name)
        self.eat = eat


class Food(Consumable):
    def __init__(self, name, eat):
        super(Food, self).__init__(name, eat)


class Froyo(Food):
    def __init__(self):
        super(Froyo, self).__init__("frozen yogurt", True)


class Sushi(Food):
    def __init__(self):
        super(Sushi, self).__init__("sushi", True)


class Candy(Food):
    def __init__(self):
        super(Candy, self).__init__("candy", True)


class Popcorn(Food):
    def __init__(self):
        super(Popcorn, self).__init__("popcorn", True)


class Grilled_Chicken(Food):
    def __init__(self):
        super(Grilled_Chicken, self).__init__("grilled chicken", True)


class Snacks(Food):
    def __init__(self):
        super(Snacks, self).__init__("random snacks", True)


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


class Soda(Drinks):
    def __init__(self):
        super(Soda, self).__init__("soda")


class Beer(Drinks):
    def __init__(self):
        super(Beer, self).__init__("beer")


class Weapon(Item):
    def __init__(self, name, attack_damage):
        super(Weapon, self).__init__(name)
        self.durability = 100
        self.attack_damage = attack_damage

    def attack(self, target):
        print("You attacked %s." % target.name)
        self.durability -= 5
        print(self.durability)
        target.take_damage(self.attack_damage)


class Stick(Weapon):
    def __init__(self):
        super(Stick, self).__init__("stick", 5)


class Spoon(Weapon):
    def __init__(self):
        super(Spoon, self).__init__("spoon", 5)

    def throw(self, target):
        print("You throw the %s at %s." % (self.name, target.name))
        self.attack(target)


class Readable(Item):
    def __init__(self, name):
        super(Readable, self).__init__(name)


class Book(Readable):
    def __init__(self):
        super(Book, self).__init__("book")


class Flower(Item):
    def __init__(self):
        super(Flower, self).__init__("flower")


class Money(Item):
    def __init__(self):
        super(Money, self).__init__("money")


class Keys(Item):
    def __init__(self, name):
        super(Keys, self).__init__(name)


class Key1(Keys):
    def __init__(self):
        super(Key1, self).__init__("key1")


class Key2(Keys):
    def __init__(self):
        super(Key2, self).__init__("key2")


class Key3(Keys):
    def __init__(self):
        super(Key3, self).__init__("key3")


class TV(Item):
    def __init__(self):
        super(TV, self).__init__("TV")


class Water_Slide(Item):
    def __init__(self):
        super(Water_Slide, self).__init__("water slide")


class Bamboo(Consumable):
    def __init__(self):
        super(Bamboo, self).__init__("bamboo", True)


class Bean_Bag(Item):
    def __init__(self):
        super(Bean_Bag, self).__init__("bean bag")


class Towel(Item):
    def __init__(self):
        super(Towel, self).__init__("towel")


class Plants(Item):
    def __init__(self):
        super(Plants, self).__init__("plants")


class Computer(Item):
    def __init__(self):
        super(Computer, self).__init__("computer")


class Treadmill(Item):
    def __init__(self):
        super(Treadmill, self).__init__("treadmill")


class Teddy(Item):
    def __init__(self):
        super(Teddy, self).__init__("teddy bear")


class Go_Cart(Item):
    def __init__(self):
        super(Go_Cart, self).__init__("go cart")


class Poster(Item):
    def __init__(self):
        super(Poster, self).__init__("poster")


class Ball(Item):
    def __init__(self):
        super(Ball, self).__init__("ball")


class Nail_Polish(Item):
    def __init__(self):
        super(Nail_Polish, self).__init__("nail polish")


class Mirror(Item):
    def __init__(self):
        super(Mirror, self).__init__("mirror")

class Door(Item):
    def __init__(self, name, locked):
        super(Door, self).__init__(name)
        self.locked = locked


class Trapdoor(Door):
    def __init__(self):
        super(Trapdoor, self).__init__("trap door", True)


class Character(object):
    def __init__(self, name, attack, description, status, clothing):
        self.name = name
        self.attack_amt = attack
        self.description = description
        self.status = status
        self.health = 100
        self.inventory = []
        self.clothing = clothing

    def take_damage(self, dmg):
        self.health -= dmg
        print("%s has %d health left." % (self.name, self.health))


puppy = Character("puppy", 3, "It's a crazy little puppy.", "rambunctious", None)
koala = Character("koala", 4, "It's a cute little koala.", "lazy", None)
penguin = Character("penguin", 6, "It's a hungry penguin.", "pissed", None)
llama = Character("llama", 5, "It's a stinky llama.", "tired", None)
you = Character("you", 20, "It's you.", None, None)
panda = Character("panda", None, "Its a serving panda.", "working", None)
puppy_god = Character("puppy god", 50, "PUPPYYYYY GOOOODDDD.", "ANGRY", None)


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
key1 = Key1()
key2 = Key2()
key3 = Key3()
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
poster = Poster()

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
                   " door, and south is a door with strange noises behind it", None, [flower])

Koala_Corner = Room("Koala Corner", "Flower_Room", None, "Garden_Room", None, None, "Puppy_Corner", None,
                    "Penguin_Corner", None, None, None,  "Koalas fill the room, one koala plays with what looks like"
                    " something you may need. There are doors north and east", koala, [bamboo, key1])

Twilight_Library = Room("Twilight Library", "Puppy_Corner", "Bean_Bag_Room", "Computer_Room", "Froyo_Room", None, None,
                        None, None, None, None, None, "The library is full of all the different genres of books, most "
                        "book are the Twilight series.There are doors north, south, east, and west. There is a book"
                        " that has a picture of the maze on the cover", None, [book])

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
                   "are doors north, east, and west. There is a staircase leading down to the south", None, [poster])

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
                    " that could be of your use. There are doors south, east, and west.", llama, [key2])

Bathroom2 = Room("Bathroom2", "Llama_Corner", None, None, "Clothes_Closet", None, None, None, None, None, None, None,
                 "Its a clean bathroom with shower access. There are doors north and west.", None, [towel])

Sushi_Room = Room("Sushi Room", "Party_Room", "Penguin_Corner", None, "Mirror_Room", None, None, None, None, None, None,
                  None, "The room is filled with a fish odor and barstools for eating. There are doors north, south,"
                  " and west.", None, [sushi, water, soda])

Penguin_Corner = Room("Penguin Corner", "Sushi_Room", None, "Money_Room", "Loser_layer", None, None, "Koala_Corner",
                      None, None, None, None, "The room is filled with snow and penguins. One penguin carries something"
                      " between its legs. There are doors north, east, and west", penguin, [key3])

print("Access your controls but typing 'controls'")
print("You also have objectives to gain points, access them bye typing 'objectives'")
print()
current_node = Puppy_Corner
directions = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southwest', 'southeast', 'up1', 'up2', 'up3']
short_direction = ['n', 's', 'e', 'w', 'ne', 'nw', 'sw', 'se', 'u1', 'u2', 'u3']
book_read = False
game_points = 0

print_room_info(current_node)

while True:
    print()
    command = input('>_').lower()

    if command == 'quit':
        quit(0)

    if command in short_direction:
        pos = short_direction.index(command)
        command = directions[pos]

    if "take" in command:
        item_requested = command[5:]
        found = False
        for item in current_node.item:
            if item.name == item_requested:
                you.inventory.append(item)
                print("You now have a %s in your inventory." % item.name)
                found = True
                current_node.item.remove(item)
                if isinstance(item, Keys):
                    game_points += 10
                    print("You earn 10 points.")
        if not found:
            print("I don't see it here.")

    elif "inventory" in command:
        for item in you.inventory:
            print(item.name)
        if len(you.inventory) == 0:
            print("There is nothing in your inventory.")

    elif "drink" in command:
        item_requested = command[6:]
        found = False
        for item in you.inventory:
            if item.name == item_requested:
                found = True
                if isinstance(item, Consumable):
                    print("You drank %s." % item.name)
                    print("You earned 5 points")
                    game_points += 5
                    you.inventory.remove(item)
                else:
                    print("You cannot drink this.")
        if not found:
            print("You don't have a %s." % item_requested)

    elif "eat" in command:
        item_requested = command[4:]
        found = False
        for item in you.inventory:
            if item.name == item_requested:
                found = True
                if isinstance(item, Consumable):
                    print("You ate %s." % item.name)
                    print("You earned 5 points")
                    game_points += 5
                    you.inventory.remove(item)
                else:
                    print("You cannot eat this.")
        if not found:
                print("You don't have %s." % item_requested)

    elif "look" in command:
        print_room_info(current_node)

    elif "game points" in command:
        print(game_points)

    elif "drop" in command:
        item_requested = command[5:]
        found = False
        for item in you.inventory:
            if item.name == item_requested:
                print("You dropped %s." % item.name)
                found = True
                you.inventory.remove(item)
            if not found:
                print("You don't have %s" % item_requested)

    elif "wear" in command:
        item_requested = command[5:]
        found = False
        for item in you.inventory:
            if item.name == item_requested:
                found = True
                if isinstance(item, Wearable):
                    print("You put on a %s." % item.name)
                    print("You earned 3 points")
                    game_points += 3
                    you.inventory.remove(item)
            else:
                print("You cannot wear this.")
        if not found:
            print("You do not have %s." % item_requested)

    elif "read" in command:
        item_requested = command[5:]
        found = False
        for item in you.inventory:
            if item.name == item_requested:
                found = True
                if isinstance(item, Readable):
                    if not book_read:
                        game_points += 5
                        print("You gain 5 points")
                    book_read = True
                    print("The book says:")
                    print("Hello, you are in the corner maze map. Your goal in the game is to find all the keys and "
                          "unlock whats behind the trap door in Puppy Corner. Good luck and don't get lost! *tip* You "
                          "might want to write down the maze on a piece of paper.")
            else:
                print("You cannot read this.")
        if not found:
            print("You do not have %s." % item_requested)

    elif "unlock" in command and current_node == Puppy_Corner:
        if key1 in you.inventory and key2 in you.inventory and key3 in you.inventory:
            print("You used your keys")
            you.inventory.remove(key1)
            you.inventory.remove(key2)
            you.inventory.remove(key3)
            print()
            current_node = Trap_Door
            print(print_room_info(current_node))
        else:
            print("You do not have all the keys")

    elif "throw" in command:
        item_requested = command[6:]
        found = False
        for item in you.inventory:
            if item.name == item_requested:
                found = True
                target_requested = input("Who do you want to hit?")
                target = None
                if current_node.characters is not None and current_node.characters.name.lower() == target_requested.\
                        lower():
                    target = current_node.characters
                    if target_requested.lower() == puppy_god.name.lower():
                        print("He ate the item")
                if target is None:
                    print("They aren't here.")
                else:
                    item.throw(target)
        if not found:
                print("You don't have %s." % item_requested)

    elif "punch" in command:
        target_requested = input("Who do you want to hit?")
        target = None
        if current_node.characters is not None and current_node.characters.name.lower() == target_requested.lower():
            target = current_node.characters
            if target_requested.lower() == puppy_god.name.lower():
                print("You instantly died from his self defense.")
                quit(0)
            target.take_damage(you.attack_amt)
        if target is None:
            print("They aren't here.")

    elif "hug" in command:
        if current_node.characters is puppy_god:
            print("You hugged puppy god")
            print("You gained 5 points")
            print("You and Puppy God are friends")
            print("game over")
            quit(0)
            game_points += 5
        if current_node.characters is not puppy_god:
            print("You hugged the %s" % current_node.characters.name)
    #
    # elif "give" in command:
    #     target_requested = input("What do you want to give?")
    #     if item in you.inventory

    elif "controls" in command:
        print("You can see your inventory if you type 'inventory.'")
        print("You can take, throw, eat, drink items by typing the command and item.")
        print("Type 'look' to get room info.")
        print("You can wear any item of clothing or jewelery.")
        print("Access your objectives by typing 'objectives'.")
        print("Check your game points by typing 'game points'.")
        print("You can hug others.")

    elif "objectives" in command:
        print("Read book")
        print("Collect Key1")
        print("Collect Key2")
        print("Collect Key3")
        print("Eat food")
        print("Drink refreshments")
        print("Wear an item of clothing")
        print("Share a sweet with puppy god")
        print("Punch a llama")
        print("Hug puppy god")

    elif command in directions:
        try:
            current_node.move(command)
            print_room_info(current_node)
        except KeyError:
            print("You cannot go this way.")

    else:
        print("Command not recognized.")
        print()
