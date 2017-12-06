import random
num = random.randint(1,50)
print(num)


print("Try to guess a random number 1-50.")
print("You have 5 guesses.")
print("Good luck!")

guess = input("What is your guess?")
print(guess == str(num))


def guess(num):
    if num == guess:
        return "Correct"
    elif num >= guess:
        return "Lower"
    elif num <= guess:
        return "Higher"



# 1. Generate random number
# 2. Take an input (number) from the user
# 3. Compare input to generated number
# 4. Add "Higher" and "Lower" statements
# 5. Add 5 guesses
