# creating a Stone,Paper,Scissors game

import random as rnd

choices = list(["stone","paper","scissors"])
def game(choices):
    final = True
    points = 0
    computer_choice = rnd.choice(choices)
    while(final):
        print("-----------------------------------------------------------")
        print("3 2 1... stone paper and scissors")
        Input = input("Enter your choice : ")
        if Input.lower() == computer_choice:
            print("You Lost !!")
            final = False
        else:
            print("You won!!")
            points += 10
            print("You have scored ",points," points")
    return points
        
result = game(choices)
print("\n \n Final Points are: ",result)