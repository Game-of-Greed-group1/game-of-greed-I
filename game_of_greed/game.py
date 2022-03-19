from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
    def __init__(self , roller=None):
        self.roller = roller
        self.banker = Banker()
        self.calculate_score = GameLogic.calculate_score
          
    def play(self):
        
        rounds = 0 
        play = input("Welcome to Game of Greed\nWanna play? ")

        if play.upper() in ["Y", "YE", "YA", "YES"]:
            play = True
        elif play.upper() in ["N", "NO","Q"]:
            play = False
        else:
            what=input("Please answer with y or n! \n>>")
            if what.upper() in ["Y", "YE", "YA", "YES"]:
                play=True
            else:
                play=False
                
        while play:
       
            if play == True:
                rounds += 1
                print(f"Starting round {rounds}")
                print("Rolling 6 dice...")
                rolling_dice = self.roller(6)
           
                nums = []
                for i in rolling_dice:
                    nums.append(str(i))
                print(",".join(nums))

            elif play.lower() in ["r"]:
                print("Rolling 6 dice...")
                rolling_dice = self.roller(6)
                
                nums = []
                for i in rolling_dice:
                    nums.append(str(i))
                print(",".join(nums))
                
            again = input("Enter dice to keep (no spaces), or (q)uit: ")
            if again == "q":
                if self.banker.balance > 0:
                    print(f"Total score is {self.banker.balance} points")
                    print(f"Thanks for playing. You earned {self.banker.balance} points")
                else:
                    print("Thanks for playing. You earned 0 points")
                break
            elif again.isdigit():
                user_input = [int(i) for i in again]
                remaining_dice = len(rolling_dice) - len(user_input)
                calculated_score = self.calculate_score(user_input)
                print(
                    f"You have {calculated_score} unbanked points and {remaining_dice} dice remaining"
                )

                roll_again = input("(r)oll again, (b)ank your points or (q)uit ")
                if roll_again == "r":
                    play = "r"
                elif roll_again == "b":
                    self.banker.shelf(calculated_score)
                    print(f"You banked {self.banker.shelved} points in round {rounds}")
                    self.banker.bank()
                    print(f"Total score is {self.banker.balance} points")
                    play = True

                elif roll_again == "q":
                    print(f"Total score is {self.banker.balance} points")
                    print(f"Thanks for playing. You earned {self.banker.balance} points")
                    break
        else:
            print("OK. Maybe another time")


if __name__ == "__main__":
    from banker import Banker
    from game_logic import GameLogic

    game = Game(GameLogic.roll_dice)
    game.play()
