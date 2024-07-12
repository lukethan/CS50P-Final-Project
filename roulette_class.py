import random
import os

class Roulette:
    choices = ["🔴", "⚫"]
    def __init__(self):
        self.number = 0
        self.color = None
        self.winnings = 0

    def bet_even(self,amount,name):
        self.spin()
        os.system('clear')
        print(f"\n\n{self.color}:{self.number}")
        if self.number % 2 == 0:
            self.winnings = amount+amount
            print(f"Good job {name}, you won {self.winnings}!")
        else:
            print("Better luck next time!")
            self.winnings = 0


    def bet_odd(self,amount,name):
        self.spin()
        os.system('clear')
        print(f"\n\n{self.color}:{self.number}")
        if self.number % 2 != 0:
            self.winnings = amount*2
            print(f"Good job {name}, you won {self.winnings}!")
        else:
            print("Better luck next time!")
            self.winnings = 0



    def bet_red(self,amount,name):
        self.spin()
        os.system('clear')
        print(f"\n\n{self.color}:{self.number}")
        if self.color == "🔴":
            self.winnings = amount*2
            print(f"Good job {name}, you won {self.winnings}!")
        else:
            print("Better luck next time!")
            self.winnings = 0



    def bet_black(self,amount,name):
        self.spin()
        os.system('clear')
        print(f"\n\n{self.color}:{self.number}")
        if self.color != "🔴":
            self.winnings = amount*2
            print(f"Good job {name}, you won {self.winnings}!")
        else:
            print("Better luck next time!")
            self.winnings = 0

    def bet_num(self,amount,name,number):
        self.spin()
        os.system('clear')
        print(f"\n\n{self.color}:{self.number}")
        if number == self.number:
            self.winnings = amount*35
            print(f"Good job {name}, you won {self.winnings}!")
        else:
            print("Better luck next time!")
            self.winnings = 0

    # def bet_color(self,balance,amount,name):
    #     ...
    # def bet_number(self,balance,amount,name):

    def spin(self):
        self.number = random.randint(0,38)
        self.color = random.choice(self.choices)



















