#encoding=utf-8

import collections
from collections import Iterable
from random import choice

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck(object):

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    #由于实现了这个方法，使得对象变成了可迭代的对象
    def __getitem__(self, item):
        return self._cards[item]

    def getCard(self):
        return self._cards

if __name__=='__main__':
    deck = FrenchDeck()
    for card in deck:
        print(card)

