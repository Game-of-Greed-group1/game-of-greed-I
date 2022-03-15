
class Game():
    def __init__(self):
        pass
    

if __name__ == "__main__":
    from game_logic import GameLogic
    from banker import Banker
    
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

    def main():
        roll = GameLogic.roll_dice()
        # scoring=GameLogic.calculate_score(roll)
        print(*roll, sep=',')
        
        return roll
    
    welcome()
    
    rounds=0
    bank = Banker() 
        
    play = input("Do you want to start the game ?! \nPlease Answer the question with y or n! \n>>")
    if play.upper() in ['Y', 'YE','YA','YES']:
        play= True
    elif play.upper() in ['N', 'NO']: 
        # print(f'If you changed your mind we always here {winking face}') 
        play=False
    else: 
        input('Please answer with y or n! \n>>') 
           
    while play:
        rounds +=1
        print(f'Starting Round {rounds}')
        print('Rolling {6} dice...')
        main()
        
        
        again = input("Would you like to play again? \n>")
        while True:
            if again.upper() in ['Y', 'YE', 'YES']:
                break
            elif again.upper() in ['N', 'NO','Q','QUIT','EX','EXIT']:
                play = False
                break
            else:
                print ('**'*20)
                again=input('Please choose your words!\nDo you want to continue playing or quit! \n>>')

    else:
        print("Thank you For playing")