from random import randint
from collections import Counter



class GameLogic:
    """
    Creating a GameLogic Class Containning The logic of Our game.
    """
    def roll_dice(n=6):
        """
        Creating Method to create a virtual dices and return a random number from 1 to 6 
        this method will create ad many dices as wanted by changeing the n value.
        For our game we will stick with 6 dices .
        
        This method will return a tuple of random numbers with length of 6 "number of dices"

        """
        return tuple([randint(1, 6) for _ in range(n)])

    @staticmethod
    def calculate_score(dices):
        """
        Creating a method  for making the rules of our game .
        This method will take the tuple of numbers of our roll_dice method as we roll the dices while playing the game.

        We made a dictionary of the rules so we can access them.
        Each value of the dice and how many repetition of the value have their own case.

        In the following code will checkk for specific rule followed from a link will attach below this doc string.

        At the end the method will return the score which is calcuated as the rules saved in the dictionary. 
        
        //search for the counte method and most_common if never heared of them
        """
        # (https://en.wikipedia.org/wiki/Dice_10000)
        rules = {
            1: {1: 100, 2: 200, 3: 1000, 4: 2000, 5: 3000, 6: 4000},
            2: {1: 0, 2: 0, 3: 200, 4: 400, 5: 600, 6: 800},
            3: {1: 0, 2: 0, 3: 300, 4: 600, 5: 900, 6: 1200},
            4: {1: 0, 2: 0, 3: 400, 4: 800, 5: 1200, 6: 1600},
            5: {1: 50, 2: 100, 3: 500, 4: 1000, 5: 1500, 6: 2000},
            6: {1: 0, 2: 0, 3: 600, 4: 1200, 5: 1800, 6: 2400},
            7: 1500,
            8: 1500,
        }

        counts = Counter(dices)
        result = counts.most_common()
        score = 0

        if len(dices) == 0:
            return 0
        if len(counts) == 6:
            return rules[7]

        if len(dices) == 6 and len(result) == 3 and result[0][1] == 2:
            return rules[8]

        for i in result:
            score += rules[i[0]][i[1]]
        return score

class Banker :
    """
    Define a Banker class to handle the scoring algorithm during the game.
    have two proprties balance, shelved and assign them to 0 for now.
    """

    def __init__(self):
        self.balance=0
        self.shelved=0
    """
    Defining a method called shelf to store the score while playing the game and before saving the round and assign it to the shelved property 
    """
    def shelf(self,point):                  
        self.shelved+=point
    """
    Defining a method called Bank to score the latest round score "from the shelved property " and add it the previous rounds score and assign it to the balance proprty. 
    
    """
    def bank(self): 
        self.balance+=self.shelved 
        self.clear_shelf() 

    """
    Defining a clear_shelf method to re assign the value in the shlved property to 0 . this way will let the next round shelved score equal to zero.
    """
    def clear_shelf(self):                      
        self.shelved=0

if __name__ == "__main__":
    def main():
        roll = GameLogic.roll_dice()
        scoring=GameLogic.calculate_score(roll)
        print(roll)
        print(scoring)
        return roll, scoring
      
    bank = Banker()     
    play = input("Do you want to start the game ?! \n>>")
    if play.upper() in ['Y', 'YE','YA','YES']:
        play= True
    elif play.upper() in ['N', 'NO']:  
        play=False
    else: 
        input('Please answer with y or n! \n>>') 
           
    while play:
        
        main()
        
        again = input("Would you like to play again? \n>")
        while True:
            if again.upper() in ['Y', 'YE', 'YES']:
                break
            elif again.upper() in ['N', 'NO']:
                play = False
                break
            else:
                "Please enter yes or no"

    else:
        print("Thank you For playing")
        
   

