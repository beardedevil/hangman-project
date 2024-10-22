#The Gallows
import random
from wordslist import words

def poor_soul(lives):
    for line in Gallows[lives]:
        print(line)

def clue(hint):
    print(" ".join(hint))

def freedom(answer):
    print(" ".join(answer))

Gallows = {0: ("   ",
               "   ",
               "   ",),
           1: (" o ",
               "   ",
               "   ",),
           2: (" o ",
               " | ",
               "   ",),
           3: (" o ",
               "/| ",
               "   ",),
           4: (" o ",
               "/|\\",
               "   ",),
           5: (" o ",
               "/|\\",
               "/  ",),
           6: (" o ",
               "/|\\",
               "/ \\",)}

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    lives = 0
    guessed_letters = set()
    playing = True
    print("Welcome Priest, Can you save this poor soul?")

    while playing:
        poor_soul(lives)
        clue(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("One letter at a time Priest!")
            continue

        if guess in guessed_letters:
            print(f"{guess} has been guessed already Priest")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for p in range(len(answer)):
                if answer[p] == guess:
                    hint[p] = guess
        else:
            lives += 1

        if "_" not in hint:
            poor_soul(lives)
            freedom(answer)
            print("You have won his freedom Priest!")
            playing = False
        elif lives >= len(Gallows) - 1:
            poor_soul(lives)
            freedom(answer)
            print("Off to the Gallows with him!")
            playing = False

    try_again()

def try_again():
    while True:
        response = input("Would you like to try to save another soul? (y/n): ").lower()
        if response == 'y':
            main()
            break
        elif response == 'n':
            print("Fare thee well, Priest!")
            break
        else:
            print("Enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
