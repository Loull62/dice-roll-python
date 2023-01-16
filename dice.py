# PYTHON DICE ROLL SIM

import random

loop = True

while loop == True:
    print("\nDice Roll Simulator Menu")

    print("1. Roll Dive Once")
    print("2. Roll Dice 5 Times")
    print("3. Roll Dice 'n' Times")
    print("4. Roll Dice until Snake Eyes")
    print("5. Exit")

    # input

    select = float(input("Select an option (1-5): "))
    dice1 = 0
    dice2 = 0

    # process

    if select == 1:
        # roll dice once
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        sum = dice1 + dice2
        print(str(dice1) + ", " + str   (dice2) + " sum: " + str(sum))
    elif select == 2:
        # roll dice five times
        for x in range(5):
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            sum = dice1 + dice2
            print(str(dice1) + ", " +   str(dice2) + " sum: " +   str(sum))
    elif select == 3:
        # roll dice n times according to user input
        rolls = int(input("How many rolls would you like? "))
        for x in range(rolls):
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            sum = dice1 + dice2
            print(str(dice1) + ", " + str(dice2) + " sum: " + str(sum))
    elif select == 4:
        # roll dice until sum on two is achieved, guaranteeing snake eyes
        eyes = False
        num = 0
        while eyes == False:
            num += 1
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            sum = dice1 + dice2
            print(str(dice1) + ", " + str(dice2) + " sum: " + str(sum))
            if sum == 2:
                eyes = True
                print("SNAKE EYES! It took "+ str(num) + " rolls to get snake eyes.")
    elif select == 5:
        # exit simulator
        loop = False
    else:
        # if user inputs a number greater than 5
        print("Not Available")