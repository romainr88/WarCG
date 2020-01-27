#!/bin/python

from random import shuffle

SUITE = 'H T C P'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        print("Creating new ordered deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling deck")
        shuffle(self.allcards)

    def split(self):
        print("Splitting deck in half")
        return self.allcards[:26],self.allcards[:26]

    pass

class Hand:

    pass

class Player:

    pass

print("Welcome to War, let's begin...")

d = Deck()
d.shuffle()
half1,half2 = d.split()
print(half1)
print(half2)
