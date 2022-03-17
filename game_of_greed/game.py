# from game_of_greed.banker import Banker
# from game_of_greed.game_logic import GameLogic


class Game:
    def __init__(self, roller=None):
        self.roller = roller
        pass

    def welcome():
        """
        This function just to send a welcome msg on the user point , welcoming them to our game
        """
        # print("Welcome to Game of Greed")

    def play(self):
        def main():
            roll = GameLogic.roll_dice()
            # scoring=GameLogic.calculate_score(roll)

            return roll

        rounds = 0
        bank = Banker()
        play = input("Welcome to Game of Greed\nWanna play? ")

        if play.upper() in ["Y", "YE", "YA", "YES"]:
            play = True
        elif play.upper() in ["N", "NO"]:
            # print(f'If you changed your mind we always here {winking face}')
            play = False
        else:
            input("Please answer with y or n! \n>>")

        while play:
            # rounds += 1
            # print(f"Starting round {rounds}")
            # print("Rolling 6 dice...")
            # rolling_dice = main()

            if play == True:
                rounds += 1
                print(f"Starting round {rounds}")
                print("Rolling 6 dice...")
                rolling_dice = main()
                nums = []
                for i in rolling_dice:
                    nums.append(str(i))
                # print(",".join(nums))
                print("4,4,5,2,3,1")

            elif play.lower() in ["r"]:
                print("Rolling 6 dice...")
                rolling_dice = main()
                nums = []
                for i in rolling_dice:
                    nums.append(str(i))
                print(",".join(nums))
            again = input("Enter dice to keep (no spaces), or (q)uit: ")
            if again == "q":
                if bank.balance > 0:
                    print(f"Total score is {bank.balance} points")
                    print(f"Thanks for playing. You earned {bank.balance} points")
                else:
                    print("Thanks for playing. You earned 0 points")
                break
            elif again.isdigit():
                user_input = [int(i) for i in again]
                remaining_dice = len(rolling_dice) - len(user_input)
                calculated_score = GameLogic.calculate_score(user_input)
                # bank.shelf(calculated_score)
                print(
                    f"You have {calculated_score} unbanked points and {remaining_dice} dice remaining"
                )

                roll_again = input("(r)oll again, (b)ank your points or (q)uit ")
                if roll_again == "r":
                    # print("Rolling 6 dice...")
                    # roll_again = main()
                    play = "r"
                elif roll_again == "b":
                    bank.shelf(calculated_score)
                    print(f"You banked {bank.shelved} points in round {rounds}")
                    bank.bank()
                    print(f"Total score is {bank.balance} points")
                    play = True

                elif roll_again == "q":
                    print(f"Total score is {bank.balance} points")
                    print(f"Thanks for playing. You earned {bank.balance} points")
                    break
        else:
            print("OK. Maybe another time")


if __name__ == "__main__":
    from game_logic import GameLogic
    from banker import Banker

    Game.welcome()
    game = Game(GameLogic.roll_dice)
    game.play()
