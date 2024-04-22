"""
This is the main code of my program, Guess the number !!!
"""
import random

# selectores
secretNumber= random.randrange(1, 100)
flag= True


# main function
while flag:
    name= int(input("I'ts your turn, please guess the number, write it down here:"))
    print(name)
    if name == secretNumber:
        print("Congratulations! You won...")
        flag= False
    else:
        print('Sorry, keep trying')
