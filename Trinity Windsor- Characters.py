class Character(object):
    def __init__(self, name, attack, description, status):
        self.name = name
        self.attack_amt = attack
        self.description = description
        self.status = status
        self.health = 100

    def attack(self, target):
        target.damage(self.attack_amt)

    def damage(self, dmg):
        self.health -= dmg


# player = Character("You", 50, "It's you", None)
# enemy = Character("Enemy", 20, "It's a bad guy", None)
#
# player.attack(enemy)
# print(enemy.health)
# enemy.attack(player)
# print(player.health)

puppy = Character("puppy", 3, "It's a crazy little puppy.", "rambunctious")
koala = Character("koala", 4, "It's a cute little koala", "lazy")
penguin = Character("penguin", 6, "It's a hungry penguin", "pissed")
llama = Character("llama", 5, "It's a stinky llama", "tired")
