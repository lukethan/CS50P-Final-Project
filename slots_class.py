import random
import os


class Slot():
    char = ["⭐","🍒","🍀"]
    # char = ["⭐"]
    def __init__(self):
        self.first = 0
        self.second = 0
        self.third = 0
        self.winnings = 0

    def play(self,amount, name):
        self.first = random.choice(self.char)
        self.second = random.choice(self.char)
        self.third = random.choice(self.char)
        os.system('clear')
        print(f"\n\n{self.first}|{self.second}|{self.third}")
        if self.first == self.second == self.third:
            self.winnings = int(amount*5)
            print(f"Congrats {name}, YOU JUST WON ${self.winnings}!!!!!")
        else:
            self.winnings = 0
            print("Better luck next time!")

    # def play(cls, balance, amount):
    #     first = random.choice(char)
    #     second = random.choice(char)
    #     third = random.choice(char)
    #     print(f"{first}|{second}|{third}")
    #     if first == second == third:
    #         winnings = int(amount*5)
    #         print(f"YOU JUST WON ${winnings}!!!!!")
    #         balance += winnings
    #         return cls(balance)
    #     else:
    #         return cls(balance)

