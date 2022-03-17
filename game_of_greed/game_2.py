from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic


class Game:
    count_rounds = 0
    rolled_dices = []

    def __init__(self, roller=None):
        self.roller = roller

    def play(self):

        bank = Banker()

        def print_new_round(func):
            def wrapper(do_not_roll_again=True):
                if do_not_roll_again:
                    self.count_rounds += 1
                    print(f"Starting round {self.count_rounds}")

                print("Rolling 6 dice...")
                rolled_dice = func()
                user_input = input("Enter dice to keep (no spaces), or (q)uit: ")
                return user_input, rolled_dice

            return wrapper

        @print_new_round
        def start_rolling():
            rolled_dice = GameLogic.roll_dice()
            nums = [str(i) for i in rolled_dice]
            print(",".join(nums))
            # rolled_dice = []
            # i = 0
            # while True:
            #     # round = 0 , index = 0
            #     # print(self.rolled_dices[i])
            #     rolled_dice = self.rolled_dices[i]
            #     nums = [str(i) for i in rolled_dice]
            #     print(",".join(nums))
            #     self.rolled_dices.pop(0)
            #     break

            return rolled_dice

        def user_decision(user_chosen_dices, rolled_dice):
            chosen_dices = [int(i) for i in user_chosen_dices]
            remaining_dices = len(rolled_dice) - len(chosen_dices)
            calculated_score = GameLogic.calculate_score(chosen_dices)
            bank.shelf(calculated_score)
            print(
                f"You have {bank.shelved} unbanked points and {remaining_dices} dice remaining"
            )

            roll_bank_quit = input("(r)oll again, (b)ank your points or (q)uit ")

            if roll_bank_quit == "b":
                if_banked()
                bank.clear_shelf()
                return

            if roll_bank_quit == "r":
                user_input, rolled_dice = start_rolling(False)
                return user_decision(user_input, rolled_dice)

            if roll_bank_quit == "q":
                print(f"Total score is {bank.balance} points")
                print(f"Thanks for playing. You earned {bank.balance} points")
                return True

        def if_banked():
            print(f"You banked {bank.shelved} points in round {self.count_rounds}")
            bank.bank()
            print(f"Total score is {bank.balance} points")

        def one_and_done():
            print("Thanks for playing. You earned 0 points")

        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")

        if wanna_play.upper() == "N":
            print("OK. Maybe another time")
            return

        if wanna_play.upper() == "Y":
            while True:
                user_input, rolled_dice = start_rolling()

                if user_input.upper() == "Q":
                    if self.count_rounds == 1:
                        one_and_done()
                    break

                quit = user_decision(user_input, rolled_dice)
                if quit:
                    break


if __name__ == "__main__":
    from game_logic import GameLogic
    from banker import Banker

    game = Game(GameLogic.roll_dice)
    game.play()
