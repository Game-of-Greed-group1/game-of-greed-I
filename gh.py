from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from collections import Counter

class Game:
    def __init__(self, roller=None, dice_roll_score=None):
        self.roller = roller  
        self.dice_roll_score = dice_roll_score
        self.banker = Banker()

    def play(self):
        # self.current_decision_score = 0
        # self.current_unbanked_score = 0
        # self.total_banked_score = 0
        self.banker.clear_shelf()
        numof_rolled_dice = 6
        round_count = 1
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")

        else:
            print(f"Starting round {round_count}")
            rolled_dice = self.roller(numof_rolled_dice)
            print(f"Rolling {numof_rolled_dice} dice...")
            
            nums = []
            for i in rolled_dice:
                nums.append(str(i))
            print(",".join(nums))
 
            
            
            while True:
                # print('we are heere')
                # print(type(rolled_dice))
                # print(self.dice_roll_score(rolled_dice))
                zilch=self.dice_roll_score(rolled_dice)
                if (zilch == 0):
                    print('Zilch!!! Round over')
                    print(f'You banked 0 points in round {round_count}')
                    print(f'Total score is 0 points')
                else:
                    print(f'{round_count} out of zilch')
                    decision = input("Enter dice to keep (no spaces), or (q)uit: ")

                    if decision == "q":

                        if self.banker.balance == 0:
                            print("Thanks for playing. You earned 0 points")
                        # print(
                        #     f"Thanks for playing. You earned {self.total_banked_score}  points"
                        # )
                        else:
                            print(f"Total score is {self.banker.balance} points")
                            print(
                                f"Thanks for playing. You earned {self.banker.balance} points"
                            )
                            self.banker.clear_shelf()
                        break

                    elif decision == "b":

                        # self.x = GameLogic.calculate_score(self.dice_roll_score)
                        # print(
                        #     f"You banked {self.current_unbanked_score} points in round {round_count} "
                        # )
                        shelfed = self.banker.shelved
                        self.banker.bank()
                        print(f"You banked {shelfed} points in round {round_count}")
                        # self.total_banked_score += self.current_decision_score

                        print(f"Total score is {self.banker.balance} points")
                        choice_message = "Enter dice to keep (no spaces), or (q)uit: "
                        # print("check_tuple########", decision)
                        round_count += 1
                        round_message = f"Starting round {round_count}"
                        print(round_message)
                        # self.current_decision_score = 0
                        # self.current_unbanked_score = 0

                        numof_rolled_dice = 6
                        rolled_dice = self.roller(numof_rolled_dice)
                        print(f"Rolling {numof_rolled_dice} dice...")
                        nums = []
                        for i in rolled_dice:
                            nums.append(str(i))
                        print(",".join(nums))

                    elif decision == "r":
                        print('score',score_decision)
                        if score_decision:
                            choice_message = "Enter dice to keep (no spaces), or (q)uit: "
                            rolled_dice = self.roller(numof_rolled_dice)

                            print(f"Rolling {numof_rolled_dice} dice...")
                            nums = []
                            for i in rolled_dice:
                                nums.append(str(i))
                            print(",".join(nums))
                            if numof_rolled_dice == 0:
                                numof_rolled_dice = 6
                        else:
                            print('Ghaida Zilch2')
                    else:
                        
                        print('av',list(rolled_dice))
                        decision = [int(x) for x in decision]
                        print('choosen',decision)
                        
                        roll = Counter(rolled_dice)  # {5:2, 2:2 , 3:1 ,4:1}
                        inputs = Counter(decision).most_common()  # [(5,3)]

                        for i in inputs:
                        
                            if roll[i[0]] and i[1] <= roll[i[0]]:  # if roll[5] and 3 <= roll[5]
                                continue
                            return  False
                        return True
                        print('hi')
                        if True:
                            
                            # for i in decision:
                            #     if i in list(rolled_dice):
                            #         list(rolled_dice).remove(i)
                            #         return list(rolled_dice)
                            # print(list(rolled_dice))        
                            x=[i for i in rolled_dice if decision in list(rolled_dice)]
                            # Counter(tuple(x))
                            # x=[i for i in Counter(rolled_dice) in Counter(decision)]
                            print(x)
                            # self.dice_roll_score = decision
                            # self.current_decision_score += GameLogic.calculate_score(
                            #     self.dice_roll_score
                            # )
                            if len(x)>0:
                                numof_rolled_dice -= len(decision)
                                # self.total_banked_score += self.current_decision_score
                                # self.current_unbanked_score += self.current_decision_score
                                score_decision = self.dice_roll_score(decision)
                                self.banker.shelf(score_decision)
                                print(
                                    f"You have {self.banker.shelved} unbanked points and {numof_rolled_dice} dice remaining"
                                )
                                wanna_play='y'
                                choice_message = "(r)oll again, (b)ank your points or (q)uit "
                                # self.current_decision_score = 0

                                # print("check_tuple########", decision)
                                if numof_rolled_dice == 0:
                                    numof_rolled_dice = 6
                                    
                            else:
                                print('Cheater')        


if __name__ == "__main__":

    from game_of_greed.game_logic import GameLogic

    game = Game(GameLogic.roll_dice, GameLogic.calculate_score)

    game.play()