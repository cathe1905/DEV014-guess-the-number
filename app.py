"""
This is the main code of my program, Guess the number !!!
"""
import random
import time


# Functions
def get_guess_Player():
       print("##### Player's turn ####")
       time.sleep(2)
       number= int(input("I'ts your turn, please guess the number, write it down here:"))
       print(number)
       return number

def get_guess_computer():
      print("##### Computer's turn ####")
      time.sleep(2)
      computerNumber= random.randint(1, 100)
      print(computerNumber)
      return computerNumber
   
def mainFunction(secretNumber=None):
    if secretNumber is None:
        secretNumber= random.randint(1, 100)
    flag= True
    while flag:
        player_guess= get_guess_Player()
        time.sleep(2)
        if player_guess == secretNumber:
            print("Congratulations! You won...")
            flag= False
            break
        else:
            if player_guess > secretNumber:
                print('Too high')
            else:
                print('Too low')

        computer_guess= get_guess_computer()
        time.sleep(2)
        if computer_guess == secretNumber:
            print("Congratulations! You won...")
            flag= False
            break
        else:
            if computer_guess > secretNumber:
                print('Too higth')
            else:
                print('Too low')
       

if __name__ == '__main__':
    mainFunction()
