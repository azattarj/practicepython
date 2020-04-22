"""Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""


from random import randint
from sys import exit


class GuessingGame:
    guess = None
    random = None
    count = 0

    def guessing(self):
        while True:
            self.guess = input('What is your guess?').lower().strip()
            try:
                self.guess = int(self.guess)
                if 1 <= self.guess <= 9:
                    self.count += 1
                    break
            except ValueError:
                if self.guess == 'exit':
                    exit()
            print('Wrong input')

    def randomizing(self):
        self.random = randint(1, 9)


while True:
    new_game = GuessingGame()
    print('Starting new guessing game. Guess between 1, 9!')
    new_game.randomizing()
    while new_game.guess != new_game.random:
        new_game.guessing()
        if new_game.guess < new_game.random:
            print('Your guess is low.')
            continue
        elif new_game.guess > new_game.random:
            print('Your guess is high.')
            continue
    else:
        print('You got it.')
        print('And it only took you', new_game.count, 'tries!')
