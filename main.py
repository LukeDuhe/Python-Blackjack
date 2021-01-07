from shoe import Shoe
from player import Player


def print_game_state(hide_dealer_hand):
    print("\n--------------------------\n")
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

def print_squiggle_message(body):
    print("\n~~~~~~~~~~~~~~~~~~~~~~")
    print(body)
    print("~~~~~~~~~~~~~~~~~~~~~~\n")


my_shoe = Shoe()

while True:
    player_one = Player()
    dealer = Player()

    dealer.add_to_hand(my_shoe.draw())
    dealer.add_to_hand(my_shoe.draw())
    player_one.add_to_hand(my_shoe.draw())
    player_one.add_to_hand(my_shoe.draw())


    print("\nRound Start!!!")

    while player_one.total < 22:

        print_game_state(True)

        valid_input = False
        move = ""
        while not valid_input:
            move = input("Would you like to [h]it or [s]tay?\n")
            if move in ["hit","h","stay","s"]:
                valid_input = True

        if move == "h" or move == "hit":
            player_one.add_to_hand(my_shoe.draw())
            print("\n\"HIT ME!\"")

        elif move == "s" or move == "stay":
            print("\n\"I'll stay.\"")
            break


    if player_one.total > 21:
        print_game_state(False)
        print_squiggle_message("YOU BUSTED!\nYOU LOSE!")
    elif player_one.total == 21:
        print_squiggle_message("YOU GOT 21!\nYOU WIN!")
    else:
        while dealer.total <= 16:
            dealer.add_to_hand(my_shoe.draw())

        print("Revealing final hands...")
        print_game_state(False)

        if dealer.total > 21:
            print_squiggle_message("THE DEALER BUSTED!\nYOU WIN!")
        elif dealer.total > player_one.total:
            print_squiggle_message("YOU LOSE!")
        elif dealer.total < player_one.total:
            print_squiggle_message("YOU WIN!")
        else:
            print_squiggle_message("IT'S A DRAW!")


    valid_input = False
    decision = ""
    while not valid_input:
        decision = input("Play again?  Y or N\n")
        if decision in ["Y","y","N","n"]:
            valid_input = True
    
    if decision == "N" or decision == "n":
        print_squiggle_message("Thanks for playing!")
        break


    if sum(my_shoe._cards.values()) < 26:
        print_squiggle_message("Reshuffling shoe...")
        my_shoe.shuffle()
