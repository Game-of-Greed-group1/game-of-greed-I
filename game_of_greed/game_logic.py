from random import randint 

class GameLogic:

    def roll_dice():
        return tuple([randint(1,6) for _ in range(6)])