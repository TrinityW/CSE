import random
num = random.randint(1,50)
print(num)


print("Try to guess a random number 1-50.")
print("You have 5 guesses.")
print("Good luck!")

guess = input("What is your guess?")
# print(guess == str(num))
if guess == str(num):
    print("Correct")
elif guess >= str(num):
    print("Lower")
elif guess <= str(num):
    print("Higher")

guess1 = input("Uh oh. Try again")
print("4 tries left")
if guess == str(num):
    print("Correct")
elif guess >= str(num):
    print("Lower")
elif guess <= str(num):
    print("Higher")

guess2 = input("Uh oh. Try again")
print("3 tries left")
if guess == str(num):
    print("Correct")
elif guess >= str(num):
    print("Lower")
elif guess <= str(num):
    print("Higher")

guess3 = input("Uh oh. Try again")

# 1. Generate random number
# 2. Take an input (number) from the user
# 3. Compare input to generated number
# 4. Add "Higher" and "Lower" statements
# 5. Add 5 guesses
