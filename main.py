from shoe import Shoe
from player import Player

my_shoe = Shoe()
player_one = Player()


while player_one.total < 22:
    player_one.add_to_hand(my_shoe.draw())
    print(player_one.hand)
    print(player_one.total)
    print()
