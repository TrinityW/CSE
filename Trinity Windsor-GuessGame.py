import random
num = random.randint(0,50)
print(num)


print("Try to guess a random number 0-50.")
print("You have 5 guesses.")
print("Good luck!")

for x in range(5):
    guess1 = input("What is your guess?")

    if guess1 == str(num):
        print("Correct")
        quit()
    elif guess1 >= str(num):
        print("Lower")
    elif guess1 <= str(num):
        print("Higher")


# print(guess == str(num))
# 1. Generate random number
# 2. Take an input (number) from the user
# 3. Compare input to generated number
# 4. Add "Higher" and "Lower" statements
# 5. Add 5 guesses
