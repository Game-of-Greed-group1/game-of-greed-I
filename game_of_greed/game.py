from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from collections import Counter
class Game:
    def __init__(self , roller=None):
        self.roller = roller
        self.banker = Banker()
        self.calculate_score = GameLogic.calculate_score
        
    @staticmethod
    def is_chosen_values_exist(dices, user_inputs):

        roll = Counter(dices)  # {5:2, 2:2 , 3:1 ,4:1}
        inputs = Counter(user_inputs).most_common()  # [(5,3)]

        for i in inputs:
           
            if roll[i[0]] and i[1] <= roll[i[0]]:  # if roll[5] and 3 <= roll[5]
                continue
            return False
        return True
      
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
                                       
            elif play.lower() in ["r"]:
                print(f"Rolling {remaining_dice} dice...")
                rolling_dice = self.roller(remaining_dice)
            else:
                pass    
            rolls = []
            for i in rolling_dice:
                rolls.append(str(i))
            print(",".join(rolls))
            
            is_zilch = self.calculate_score(rolling_dice)
            if  is_zilch:  
                again = input("Enter dice to keep (no spaces), or (q)uit: ")
                
                if again == "q":
                    
<<<<<<< HEAD
                    if self.banker.balance > 0 or rounds > 1:
=======
                    if self.banker.balance > 0 or rounds > 1 :
>>>>>>> 9fb2bb2e048b250d56489f1afe610cc95a06c29b
                        print(f"Total score is {self.banker.balance} points")
                        print(f"Thanks for playing. You earned {self.banker.balance} points")
                    else:
                        print("Thanks for playing. You earned 0 points")
                    break
                elif again.isdigit():
                    
                    rolls=[int(i)for i in rolls]
                    user_input = [int(i) for i in again]
                    check =  Game.is_chosen_values_exist(rolls,user_input)
                    
                    if check:
                        value=self.calculate_score(user_input)
                        if value:
                            remaining_dice = len(rolling_dice) - len(user_input)
                            self.banker.shelf(value)
                            print(f"You have {self.banker.shelved} unbanked points and {remaining_dice} dice remaining")
                            if self.calculate_score(user_input) and remaining_dice == 0:
                                remaining_dice=6

                            roll_again = input("(r)oll again, (b)ank your points or (q)uit ")
                            
                            if roll_again == "r":        
                                play = "r"
                                
                            elif roll_again == "b":
                                print(f"You banked {self.banker.shelved} points in round {rounds}")
                                self.banker.bank()
                                print(f"Total score is {self.banker.balance} points")
                                play = True

                            elif roll_again == "q":
                                print(f"Total score is {self.banker.balance} points")
                                print(f"Thanks for playing. You earned {self.banker.balance} points")
                                break
                        else:
                            print('You Choose a dice of value 0')
                            print('Choose Wisely')
                            play="Try again"    
                    else:
                        print('Cheater!!! Or possibly made a typo...') 
                        play="cheater, do it again"  
                else:
                    print('Cheater!!! Or possibly made a typo...') 
                    play="cheater, do it again"         
            else:
                self.banker.clear_shelf()
                print('Zilch!!! Round over')
                print(f"You banked {self.banker.shelved} points in round {rounds}")
                print(f"Total score is {self.banker.balance} points")
                play = True
                
                            
        else:
            print("OK. Maybe another time")

      
if __name__ == "__main__":
    
    from game_of_greed.game_logic import GameLogic
    from game_of_greed.banker import Banker
    
    # def welcome():
    #     """
    #     This function just to send a welcome msg on the user point , welcoming them to our game
    #     """
        
        
        # print('*'*40)
        # print ('**' + ' '*6 + 'Welcome to Game of Greed' + ' '*6 + '**')
        # print ('**' +' '*36 +  '**')
        # print ('**' + '   ' + '   Hope You Enjoy the game       ' + '**')
        # print ('**' +' '*36 +  '**')q
        # print ('**' + '   ' + '          V 1.0                  ' + '**' )
        # print ('**' +' '*36 +  '**')
        # print('*'*40)

    # def main():
    #     roll = GameLogic.roll_dice()
    #     # scoring=GameLogic.calculate_score(roll)
    #     print(*roll, sep=',')
        
    #     return roll
    
    # welcome()
    
       
    game = Game(GameLogic.roll_dice)
    game.play()
   