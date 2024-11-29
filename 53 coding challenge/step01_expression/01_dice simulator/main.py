# ## Problem Statement

# Simulate rolling two dice, three times.  Prints the results of each die roll.  This program is used to show how variable scope works.

import random

num_sides = 6


def dice_Roll():
    dice1:int = random.randint(1, num_sides)
    dice2:int = random.randint(1, num_sides)
    total_num:int = dice1 + dice2
    print("Total of two dice: ", total_num )

def main():
    dice1:int = 10
    print("dice1 in main() starts as: " + str(dice1)) #it print the initial value which is 10
    dice_Roll()
    dice_Roll()
    dice_Roll()
    print("dice1 in main() is: " + str(dice1)) #it print again after diecing roll it again prints 10


if __name__=='__main__':
    main()


