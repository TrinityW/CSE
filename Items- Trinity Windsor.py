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
        super(Froyo, self).__init__("Frozen Yogurt", True)

    def lick(self):
        print("you lick your froyo")
        

class Sushi(Food):
    def __init__(self):
        super(Sushi, self).__init__("Sushi", True)

    def barf(self):
        print("you barf because sushi is gross")
        
        
class Candy(Food):
    def __init__(self):
        super(Candy, self).__init__("Candy", True)

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

