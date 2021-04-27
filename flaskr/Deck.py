import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Card):
            return self.suit == other.suit and self.rank == other.rank
        return NotImplemented

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self):
        return "{} of {}s".format(self.rank, self.suit)

    def __repr__(self):
        return "{} of {}s".format(self.rank, self.suit)

class Deck:
    suits = ["Club", "Diamond", "Heart", "Spade"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        # Add 52 cards to the deck
        self.deck = []
        self.out = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))

    def deal(self):
        card = self.deck.pop()
        self.out.append(card)

        return card

    def shuffle(self):
        random.shuffle(self.deck)

    def shuffleBack(self):
        self.deck.extend(self.out)
        self.out = []

        self.shuffle()
