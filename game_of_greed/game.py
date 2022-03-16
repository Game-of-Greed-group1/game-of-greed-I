
from re import T


class Game():
    def __init__(self,rolling = None):
        self.rolling = rolling 
        
    def play(self):
        
        # print("Welcome to Game of Greed")
        play = input("Welcome to Game of Greed\nWanna play? ")
               
        rounds = 0   
        score = 0 
        
        if play.upper() in ['Y', 'YE','YA','YES']:
            play = True
        elif play.upper() in ['N', 'NO','Q']: 
            print("OK. Maybe another time") 
            play = False
        else: 
            play=str(input('Please answer with y or n! \n>>'))
            
            
        
        while play:
            
           
            if play ==True:
                rounds +=1
                print(f'Starting round {rounds}')
                print('Rolling 6 dice...')
                rolled_dice=self.rolling(6)
            elif play.lower() in ['r','roll']:
                print('Rolling 6 dice...')
                rolled_dice=self.rolling(6)
            
            nums = []
            for i in rolled_dice:
                nums.append(str(i))
            print(*nums, sep=',')
            
            
            decision = input("Enter dice to keep (no spaces), or (q)uit: ")
            
            if decision.isdigit() :
                
                
                d=int(decision)
                d=[int(a) for a in str(d)]
                
                scoring=GameLogic.calculate_score(d)
                
                
                if scoring !=0:
                    
                
                    score += scoring
                    shelfed=scoring
                    # score=scoring.calculate_score(d)
                    print(f'You have {shelfed} unbanked points and {len(nums)-len(d)} dice remaining')
                    decision=input('(r)oll again, (b)ank your points or (q)uit ')
                    if decision.lower() in ['r','roll']:
                        # this_round=rounds
                        play='r'
                        
                    if decision.lower() in ['b','bank']:
                        banking=Banker()
                        banking.shelf(score)
                        banked=banking.bank()

                        print(f'You banked {shelfed} points in round {rounds}')
                        print(f'Total score is {score} points')                       
                        # x=d-nums
                        # print (x)
                        play=True
                    if decision.lower() in ['q','quit']:
                        print(f"Thanks for playing. You earned {score} points") 
                        play=False              
                else:
                    print(f"Bad choice. This dice have {scoring} points \nGood Luck Next time!")
                    play=True
                        
                    
            elif decision.upper() in ['N', 'NO','Q','QUIT','EX','EXIT']:
                if score>0:
                    print(f'Total score is {score} points')                       
                print(f"Thanks for playing. You earned {score} points") 
                break
           
            elif decision.upper() in ['R', 'ROLL']:
                Play=True
            else:
                print ('**'*20)
                decision=input('Enter dice to keep (no spaces), or (q)uit: ')
   
        

if __name__ == "__main__":
    from game_logic import GameLogic
    from banker import Banker
    
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
    
    # rounds=0
    # bank = Banker()     
    game = Game(GameLogic.roll_dice)
    game.play()
    # play = input("Do you want to start the game ?! \nPlease Answer the question with y or n! \n>>")
    # if play.upper() in ['Y', 'YE','YA','YES']:
    #     play= True
    # elif play.upper() in ['N', 'NO']: 
    #     # print(f'If you changed your mind we always here {winking face}') 
    #     play=False
    # else: 
    #     input('Please answer with y or n! \n>>') 
           
    # while play:
    #     rounds +=1
    #     print(f'Starting Round {rounds}')
    #     print('Rolling {6} dice...')
    #     main()
        
    #     again = input("Would you like to play again? \n>")
    #     while True:
    #         if again.upper() in ['Y', 'YE', 'YES']:
    #             break
    #         elif again.upper() in ['N', 'NO','Q','QUIT','EX','EXIT']:
    #             play = False
    #             break
    #         else:
    #             print ('**'*20)
    #             again=input('Please choose your words!\nDo you want to continue playing or quit! \n>>')

    # else:
    #     print("Thank you For playing")