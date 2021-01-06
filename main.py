from shoe import Shoe
from player import Player

my_shoe = Shoe()
player_one = Player()
dealer = Player()


def print_game_state(hide_dealer_hand):
    print("Dealer's Hand:")
    if hide_dealer_hand:
        print(f"['{dealer.hand[0]}','----']\n")
    else:
        print( f"{dealer.hand}\n" )

    print("Dealer's Total:")
    if hide_dealer_hand:
        print("???\n\n")
    else:
        print(f"{dealer.total}\n\n")

    print("Your Hand:")
    print( f"{player_one.hand}\n" )

    print("Your Total:")
    print(player_one.total)
    print("\n--------------------------\n")


dealer.add_to_hand(my_shoe.draw())
dealer.add_to_hand(my_shoe.draw())
player_one.add_to_hand(my_shoe.draw())
player_one.add_to_hand(my_shoe.draw())

print("\nRound Start!!!")
print("--------------------------\n")


while player_one.total < 22:

    print_game_state(True)

    move = input("Would you like to [h]it or [s]tay?\n")

    if move == "h" or move == "hit":
        player_one.add_to_hand(my_shoe.draw())
        print("\nHIT ME!")
        print("--------------------------\n")

    elif move == "s" or move == "stay":
        print("\nI'll stay.")
        break

if player_one.total > 21:
    print_game_state(False)
    print("\n~~~~~~~~~~~~~~~~~~~~~~")
    print("YOU BUSTED!\nYOU LOSE!")
    print("~~~~~~~~~~~~~~~~~~~~~~\n")
elif player_one.total == 21:
    print("\n~~~~~~~~~~~~~~~~~~~~~~")
    print("BLACKJACK!\nYOU WIN!")
    print("~~~~~~~~~~~~~~~~~~~~~~\n")
else:
    while dealer.total <= 16:
        dealer.add_to_hand(my_shoe.draw())

    print("Revealing final hands...")
    print("--------------------------\n") 
    print_game_state(False)

    if dealer.total > 21:
        print("\n~~~~~~~~~~~~~~~~~~~~~~")
        print("THE DEALER BUSTED!\nYOU WIN!")
        print("~~~~~~~~~~~~~~~~~~~~~~\n")
    elif dealer.total > player_one.total:
        print("\n~~~~~~~~~~~~~~~~~~~~~~")
        print("YOU LOSE!")
        print("~~~~~~~~~~~~~~~~~~~~~~\n")
    elif dealer.total < player_one.total:
        print("\n~~~~~~~~~~~~~~~~~~~~~~")
        print("YOU WIN!")
        print("~~~~~~~~~~~~~~~~~~~~~~\n")
    else:
        print("\n~~~~~~~~~~~~~~~~~~~~~~")
        print("IT'S A DRAW!")
        print("~~~~~~~~~~~~~~~~~~~~~~\n")
