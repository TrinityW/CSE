import random
#Trinity Windsor
money = 15
rounds = 0

while money > 0:
    D1 = random.randint(1, 6)
    D2 = random.randint(1, 6)
    total = D1 + D2
    print("rolled: %s" % total)
    print("money: %s" % money)
    rounds += 1
    print(rounds)

    if D1 + D2 == 7:
        money += 4
        print(money)
    else:
        money -= 1
        print(money)

