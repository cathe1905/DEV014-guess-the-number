"""
This is the main code of my program, Guess the number !!!
"""
# Import the modules I need in my program
import random
import time

#Create two empty list which I will use in the main function
guesses_computer= []
guesses_player= []

# This function get the player guess from the input
def get_guess_Player():
       print("##### Player's turn ####")
       time.sleep(2)
       number= int(input("I'ts your turn, please guess the number, write it down here: "))
       print(number)
       return number

# This function get the computer guess from the random method
def get_guess_computer():
      print("##### Computer's turn ####")
      time.sleep(2)
      computerNumber= random.randint(1, 100)
      print(computerNumber)
      return computerNumber

# This funtion display the list of guesses of the winer
def show_guesses_winer(iterable):
    print("These were your guesses:", end=" ")
    for guess in iterable:
        print(guess, end=" ")
    print()
   
# This is the principal function, which is in charge to execute the loop for the game
def mainFunction(secretNumber=None):

    global guesses_computer, guesses_player 

    if secretNumber is None:
        secretNumber= random.randint(1, 100)

    flag= True

    while flag:
        player_guess= get_guess_Player()
        guesses_player.append(player_guess)
        time.sleep(2)
        if player_guess == secretNumber:
            print("Congratulations! You won...")
            flag= False
            show_guesses_winer(guesses_player)
            break
        else:
            if player_guess > secretNumber:
                print('Too high')
            else:
                print('Too low')

        computer_guess= get_guess_computer()
        guesses_computer.append(computer_guess)
        time.sleep(2)
        if computer_guess == secretNumber:
            print("Congratulations! You won...")
            flag= False
            show_guesses_winer(guesses_computer)
            break
        else:
            if computer_guess > secretNumber:
                print('Too higth')
            else:
                print('Too low')
        
if __name__ == '__main__':
    mainFunction()

#This block of code ask the player if they want to play again or not
ask_play_again= input('Do you want to play again? ')
if ask_play_again.lower() == "yes" or "y" or "si" or "s":
    mainFunction()