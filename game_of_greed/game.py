class Game():
    def __init__(self,rolling = None):
        self.rolling = rolling 
    def welcome():
        """
        This function just to send a welcome msg on the user point , welcoming them to our game
        """
        
        
        print('*'*40)
        print ('**' + ' '*6 + 'Welcome to Game of Greed' + ' '*6 + '**')
        print ('**' +' '*36 +  '**')
        print ('**' + '   ' + '   Hope You Enjoy the game       ' + '**')
        print ('**' +' '*36 +  '**')
        print ('**' + '   ' + '          V 1.0                  ' + '**' )
        print ('**' +' '*36 +  '**')
        print('*'*40)

      
    def play(self):
        
        print("Welcome to Game of Greed")
        play = input("Wanna play? ")
               
        rounds = 0   
        score = 0 
        
        if play.upper() in ['Y', 'YE','YA','YES']:
            play = True
        elif play.upper() in ['N', 'NO','Q']: 
            print("OK. Maybe another time") 
            play = False
        else: 
            play=str(input('Please answer with y or n! \n>>'))
            if play.upper() in ['Y','YE','YES']:
                play = True
            else :    
                play = False
           
            
            
        
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
                nums.append(int(i))
            print(*nums, sep=',')
            
            
            decision = input("Enter dice to keep (no spaces), or (q)uit: ")
            
            if decision.isdigit() :
                
                
                d=int(decision)
                d=[int(a) for a in str(d)]
                availabe_nums = [i for i in d if i in nums]
                print('av',availabe_nums)
                rest = [i for i in d if i not in nums]
                print('r',rest)
                scoring=GameLogic.calculate_score(availabe_nums)
                
                
                if scoring !=0:
                    
                    score += scoring
                    shelfed=scoring
                    print(f'You have {shelfed} unbanked points and {len(nums)-len(d)} dice remaining')
                    decision=input('(r)oll again, (b)ank your points or (q)uit ')
                    if decision.lower() in ['r','roll']:
                        play='r'
                        
                    if decision.lower() in ['b','bank']:
                        banking=Banker()
                        banking.shelf(score)
                        banking.bank()

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
    
    Game.welcome()  
    game = Game(GameLogic.roll_dice)
    game.play()
   