import random, itertools

deck = list(itertools.product(range(1, 14), ['Hearts', 'Diamonds', 'Clubs', 'Spades']))
random.shuffle(deck)
print(deck)

for i in range(10):
    print(deck[i][0], 'of', deck[i][1])