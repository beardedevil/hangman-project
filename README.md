THE GALLOWS

Welcome to The Gallows, a fun and challenging word-guessing game implemented in Python. In this game, you'll need to save a poor soul from the gallows by guessing the correct letters of a hidden word.

FEATURES

Randomly selects a word from a predefined list.
Visual representation of the gallows as you make incorrect guesses.
Keeps track of guessed letters and lives remaining.

INSTALLATION

To run the game, you'll need Python installed on your machine. You can download Python from python.org.
Clone this repository or download the script file.
Ensure you have a wordslist.py file that contains a list of words as a Python list named words.

USAGE

Open a terminal or command prompt.
Navigate to the directory containing the script.
Run the script using Python:

GAMEPLAY

You will be greeted with a welcome message.
The game will display the current state of the gallows and the clue (hidden word).
Input one letter at a time to guess the word.
You have a limited number of incorrect guesses (lives).
The game will ask if you would like to try again y/n(depending on how you answer the game will repeat or it will end).

CODE STRUCTURE

poor_soul(lives): Displays the gallows based on the number of incorrect guesses.
clue(hint): Displays the current state of the hidden word.
freedom(answer): Displays the completed word when the game is won.
main(): The main game loop that handles gameplay and user input.
try_again(): repeats main() or ends the game
