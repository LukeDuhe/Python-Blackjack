import random


class Shoe(object):
    """
    docstring
    """
    
    def __init__(self):
        self.default_cards = {
            "ace":4,
            "king":4,
            "queen":4,
            "jack":4,
            "ten":4,
            "nine":4,
            "eight":4,
            "seven":4,
            "six":4,
            "five":4,
            "four":4,
            "three":4,
            "two":4,
            "one":4
        }

        self._cards = self.default_cards

    def get_filtered_deck(self):
        deck = list(self._cards.keys())
        deck = [card for card in deck if self._cards[card] > 0]
        return deck

    def draw(self):
        available_cards = self.get_filtered_deck()
        card = random.choice(available_cards)
        self._cards[card] -= 1
        return card

    def reshuffle(self):
        self._cards = self.default_cards
