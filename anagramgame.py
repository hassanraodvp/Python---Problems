import random 
words = ["Cheap", "Laugh", "Listen", "Fights", "Friendship"]
word = random.choice(words)

jumble = "".join(random.sample(word, len(word)))

print("~~~ Guess the Corrected word ~~~")

chances = 3

while chances != 0:
    print("The word is:", jumble)
    guess = input("Enter your guess: ")
    if guess == word:
        print("Congratulations! You guessed the word correctly.")
        break
    else:
        chances -= 1
        print("Wrong guess! You have", chances, "chances left.")
else:
    print("You lost! The correct word was:", word)    