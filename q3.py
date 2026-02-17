import random
def ches():
    suits = ["♠", "♥", "♣", "♦"]
    c = random.choice(suits)
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    d = random.choice(values)
    return c, d
for i in range(5):
    print(ches)
# Make a deck of cards
# `deck` should be a list of strings with a value and a suit, e.g. "4♣"

#shuffle your `deck` and print it out

# sample a hand of 5 cards and print it out
# (WITHOUT replacement -- no repeats!)