import random


"""A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """

"""Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """
class Die:
    def __init__(self):
        self.value = 0
        self.points = 0

    """Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
    """
    def roll(self):
        x = 0
        self.value = random.randint(1,6)
        if self.value == 1:
            self.points= 50
        elif self.value == 5:
            self.points= 100
        else:
            self.points = 0
        return self.value, self.points