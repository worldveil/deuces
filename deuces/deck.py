from random import shuffle, random
from card import Card


class Deck:
    """
    Class representing a deck. The first time we create, we seed the static
    deck with the list of unique card integers. Each object instantiated simply
    makes a copy of this object and shuffles it.

    The state of a deck is defined by the random float [0.0, 1.0) used to seed
    the shuffle() operation, combined with the number of cards that have
    already been drawn.
    """
    _FULL_DECK = []

    def __init__(self, seed=None, num_drawn=0):
        if not seed:
            seed = random()
        self.seed = seed
        self.shuffle(seed)

        self.num_drawn = 0
        if num_drawn:
            self.draw(num_drawn)

    def shuffle(self, seed):
        # and then shuffle
        self.cards = Deck.GetFullDeck()
        shuffle(self.cards, lambda: seed)

    def draw(self, n=1):
        self.num_drawn += n
        if n == 1:
            return self.cards.pop(0)

        return [self.cards.pop(0) for _ in range(n)]

    def __str__(self):
        return Card.print_pretty_cards(self.cards)

    @staticmethod
    def GetFullDeck():
        if Deck._FULL_DECK:
            return list(Deck._FULL_DECK)

        # create the standard 52 card deck
        for rank in Card.STR_RANKS:
            for suit, val in Card.CHAR_SUIT_TO_INT_SUIT.iteritems():
                Deck._FULL_DECK.append(Card.new(rank + suit))

        return list(Deck._FULL_DECK)
