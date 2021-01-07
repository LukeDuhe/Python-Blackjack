class Player(object):
    """
    docstring
    """

    card_values = {
            "ace":11,
            "king":10,
            "queen":10,
            "jack":10,
            "ten":10,
            "nine":9,
            "eight":8,
            "seven":7,
            "six":6,
            "five":5,
            "four":4,
            "three":3,
            "two":2,
            "one":1
        }
    
    def __init__(self):
        self.total = 0
        self.hand = []

    def add_to_hand(self, card):
        self.hand.append(card)

        self.total = sum([self.card_values[card] for card in self.hand])

        if self.total > 21:
            self.total -= 10*self.hand.count("ace")

    def reset():
        self.total = 0
        self.hand = []
