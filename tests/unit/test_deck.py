# from Blackjack import Deck
# import Blackjack from 
# from Deck import Card, Deck
# import unittest

# suits = ["Club", "Diamond", "Heart", "Spade"]
# ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# class DeckInit(unittest.TestCase):
#     def test_has_52_cards(self):
#         test_deck = Deck()
#         self.assertEqual(len(test_deck.deck), 52)

#     def test_no_missing_cards(self):
#         test_deck = Deck()
#         cards = set([Card(suit, rank) for suit in suits for rank in ranks])

#         for card in test_deck.deck:
#             if(card in cards):
#                 cards.remove(card)

#         self.assertEqual(len(cards), 0)

#     def test_no_repeat_cards(self):
#         test_deck = Deck()
#         card_set = set(test_deck.deck)
#         self.assertEqual(len(card_set), 52)

#     def test_no_cards_outside(self):
#         test_deck = Deck()
#         self.assertEqual(len(test_deck.out), 0)

# class DeckShuffle(unittest.TestCase):
#     def test_not_inorder(self):
#         test_deck = Deck()
#         cards = [Card(suit, rank) for suit in suits for rank in ranks]
#         test_deck.shuffle()

#         inOrder = True
#         for i, card in enumerate(cards):
#             if(card != test_deck.deck[i]):
#                 inOrder = False
#                 break
                
#         self.assertFalse(inOrder)

#     def test_shuffles_differ(self):
#         test_deck1 = Deck()
#         test_deck2 = Deck()

#         test_deck1.shuffle()
#         test_deck2.shuffle()

#         sameOrder = True
#         for i, card in enumerate(test_deck1.deck):
#             if(card != test_deck2.deck[i]):
#                 sameOrder = False
#                 break

#         self.assertFalse(sameOrder)
                
# class DeckDeal(unittest.TestCase):
#     def test_deal_removes_card(self):
#         test_deck = Deck()
#         card = test_deck.deal()

#         self.assertEqual(len(test_deck.deck), 51)
#         self.assertEqual(len(test_deck.out), 1)
#         self.assertEqual(card, test_deck.out[0])

from flaskr.Deck import Deck

def test_true():
    test_deck = Deck()
    assert len(test_deck.deck) == 52

# if __name__ == "__main__":
#     unittest.main()