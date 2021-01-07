import random


class Shoe(object):
    """
    docstring
    """

    def shuffle(self):
        self._cards = {card: 4 for card in self.default_cards}
    
    def __init__(self):
        self.default_cards = ["ace", "king", "queen", "jack", "ten", "nine", 
                                "eight", "seven", "six", "five", "four", "three", "two", "one"]

        self._cards = {}
        self.shuffle()

    def get_filtered_deck(self):
        deck = list(self._cards.keys())
        deck = [card for card in deck if self._cards[card] > 0]
        return deck

    def draw(self):
        available_cards = self.get_filtered_deck()
        card = random.choice(available_cards)
        self._cards[card] -= 1
        return card
