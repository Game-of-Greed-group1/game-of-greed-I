class Banker:
    """
    Define a Banker class to handle the scoring algorithm during the game.
    have two proprties balance, shelved and assign them to 0 for now.
    """

    def __init__(self):
        self.balance = 0
        self.shelved = 0

    """
    Defining a method called shelf to store the score while playing the game and before saving the round and assign it to the shelved property 
    """

    def shelf(self, point):
        self.shelved += point

    """
    Defining a method called Bank to score the latest round score "from the shelved property " and add it the previous rounds score and assign it to the balance proprty. 
    
    """

    def bank(self):
        self.balance += self.shelved
        self.clear_shelf()

    """
    Defining a clear_shelf method to re assign the value in the shlved property to 0 . this way will let the next round shelved score equal to zero.
    """

    def clear_shelf(self):
        self.shelved = 0
