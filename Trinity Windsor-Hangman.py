import random
# import string
"""
A general guide for Hangman
1. Make a word  bank - 10 items
2. Pick a random item from the list
3. Add a guess to the list of letters guessed
4. Reveal letters already guessed
5. Create the win conditions

"""
AdventureTime_list = ["jake the dog", "fin the human", "princess bubblegum", "marceline the vampire queen", "ice king",
                      "lady rainacorn", "lumpy space princess", "gunter", "flame princess", "beemo", "tree trunks"]
# print(random.choice(AdventureTime_list))

guesses_left = 10
print(guesses_left)
word = random.choice(AdventureTime_list)
letters_guessed = []
players_guess = "true"
while players_guess != word:
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print("".join(list(output)))
    guess = input("Guess a letter: ")
    print("guesses left: %s" % guesses_left)
    letters_guessed.append(guess)
    print(", ".join(letters_guessed))

    if guess not in word:
        guesses_left -= 1
        print(guesses_left)
    if output == list(word):
        exit(0)