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
def get_guess_player():
       time.sleep(2)
       number= int(input("I'ts your turn, please guess the number, write it down here:"))
       return number

# This function get the computer guess from the random method
def get_guess_computer():
      time.sleep(2)
      computerNumber= random.randint(1, 100)
      return computerNumber

# This funtion display the list of guesses of the winer
def show_guesses_winer(iterable):
    print("These were your guesses:", end=" ")
    for guess in iterable:
        print(guess, end=" ")
    print()

#This function evaluate if the guess player o computer is equal to secret number and return true or false
def evaluate_guess(guess, number):
    if guess == number:
        print("Congratulations! You won...")
        return True
    elif guess > number:
        print('Too high')
    else:
        print('Too low')
    return False
    
# This is the principal function, which is in charge to execute the loop for the game 
def mainFunction():
    secretNumber= random.randint(1, 100) #Create a variable witch contains the secret number    
    global guesses_computer, guesses_player 
    flag_for_break_loop= True

    while flag_for_break_loop:
        print("##### Player's turn ####")
        player_guess= get_guess_player()
        guesses_player.append(player_guess)
        
        time.sleep(2)
        if evaluate_guess(player_guess, secretNumber):
            flag_for_break_loop= False
            show_guesses_winer(guesses_player)
            break
        
        print("#### Computer's turn ####")
        computer_guess= get_guess_computer()
        print(f"It's the computer's turn: {computer_guess} ")
        guesses_computer.append(computer_guess)
        time.sleep(2)
        if evaluate_guess(computer_guess, secretNumber):
            flag_for_break_loop= False
            show_guesses_winer(guesses_computer)
            break

     #This return will be used in my test     
    return flag_for_break_loop

#This block of code ask the player if they want to play again or not
def ask_play_again():
    answer_player= input('Do you want to play again? ')
    if answer_player.lower() in ["yes", "y", "si", "s"]:
        mainFunction()
    else: 
        print('See you later')
        print()
        return;
      

if __name__ == '__main__':
    mainFunction()
    ask_play_again()


