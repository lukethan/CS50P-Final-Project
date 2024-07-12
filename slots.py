
from slots_class import Slot
from player_class import Player
from roulette_class import Roulette
import os

def main():
    print("\n\nWelcome to CS_ino_50!", end="\n\n\n")
    p1 = Player.get()
    r1 = Roulette()
    s1 = Slot()
    p1.game()
    print(p1)
    while True:
        try:
            while p1.gamechoice == 1:
                # while True:
                    p1.r_bet()
                    p1.bet()
                    amount = p1.amount
                    name = p1.name
                    if p1.bet_type == "red":
                        r1.bet_red(amount, name)
                        p1.check(r1.winnings)
                    elif p1.bet_type == "black":
                        r1.bet_black(amount, name)
                        p1.check(r1.winnings)
                    elif p1.bet_type == "even":
                        r1.bet_even(amount, name)
                        p1.check(r1.winnings)
                    elif p1.bet_type == "odd":
                        r1.bet_odd(amount, name)
                        p1.check(r1.winnings)
                    elif p1.bet_type == "number":
                        num = p1.get_num()
                        r1.bet_num(amount, name, num)
                        p1.check(r1.winnings)
                    p1.game()
            while p1.gamechoice == 2:
                p1.bet()
                amount = p1.amount
                name = p1.name
                s1.play(amount, name)
                p1.check(s1.winnings)
                p1.game()

        except EOFError:
            os.system('clear')
            print(f"\nThanks for playing {p1.name}")
            print(f"Your final balance was ${p1.balance}")
            return False






# def roulette():
#     print(p1)
#     p1.bet()
#     amount = p1.amount
#     name = p1.name
#     num = p1.get_num()
#     r1.bet_num(amount, name, num)
#     p1.check(r1.winnings)

    # p1 = Player.get()
    # s1 = Slot()
    # print(p1)
    # while True:
    #     try:
    #         p1.bet()
    #         amount = p1.amount
    #         name = p1.name
    #         s1.play(amount, name)
    #         p1.check(s1.winnings)

    #     except EOFError:
    #         print("\nThanks for playing")
    #         return False


if __name__=="__main__":
    main()
