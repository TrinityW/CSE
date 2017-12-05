import random
print(random.randint(1,50))


print("Try to guess a random number 1-50.")
print("You have 5 guesses.")
print("Good luck!")

guess = input("What is your guess?")
print(guess == random.randint)


def guess(number):
    if number >= number:
        return "lower"
    elif number <= number:
        return "higher"
    elif number ==number:
        return "correct"

guess("%s" % guess)


# 1. Generate random number
# 2. Take an input (number) from the user
# 3. Compare input to generated number
# 4. Add "Higher" and "Lower" statements
# 5. Add 5 guesses
