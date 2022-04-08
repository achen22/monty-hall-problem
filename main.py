from random import randint, choice
from sys import argv

class Game:
  def __init__(self):
    self.car = randint(1, 3)
  
  def guess(self, n):
    return n == self.car

  def reveal_goat(self, guess):
    can_open = [i for i in range(1, 4) if i != self.car and i != guess]
    return choice(can_open)

if __name__ == "__main__":
  if len(argv) > 1: # command line arguments - run trials
    TRIALS = 1000
    print(f"Running {TRIALS} trials for with strategy SAME DOOR...")
    wins = 0
    for _ in range(TRIALS):
      game = Game()
      guess = randint(1, 3)
      goat = game.reveal_goat(guess)
      wins += game.guess(guess)
    print(f"Win rate: {wins} / {TRIALS} ({100 * wins / TRIALS :.2f}%)\n")

    print(f"Running {TRIALS} trials for with strategy SWITCH DOOR...")
    wins = 0
    for _ in range(TRIALS):
      game = Game()
      guess = randint(1, 3)
      goat = game.reveal_goat(guess)
      guess = [i for i in range(1, 4) if i != guess and i != goat][0]
      wins += game.guess(guess)
    print(f"Win rate: {wins} / {TRIALS} ({100 * wins / TRIALS :.2f}%)\n")

  else: # play single game
    game = Game()
    print("There are three doors (1, 2, 3).")
    print("One of these doors has a car.")
    print("The other two doors have goats.")
    print("Which door do you think has the car? ")

    n = input(">>> ")
    if n.isdigit():
      n = int(n)

    opened = game.reveal_goat(n)
    print(f"A goat is revealed to be behind door {opened}.")
    print("Now which door do you think has the car? ")

    n = input(">>> ")
    if n.isdigit():
      n = int(n)
    
    if game.guess(n):
      print("You chose correctly!")
    else:
      print(f"The car was behind door {game.car}")
