"""
This is the main code of my program, Guess the number !!!
"""
# Import the modules I need in my program
import random
import time

minimo= 1 #set the minimum range of the secret number
maximo= 100 #set the maximum range of the secret number


#classes
class Game: #class responsible for managing the game operations
    def start(self):
        global secretNumber
        secretNumber= random.randint(1, 100) #Create a variable witch contains the secret number 
        print("Game started!")
  
   #This function evaluate if the guess player or computer is equal to secret number and return true or false
    def evaluate_guess(self, guess, number):
        if guess == number:
            print("Congratulations! You won...")
            return True
        elif guess > number:
            print('Too high')
        else:
            print('Too low')
        return False

    # This funtion display the list of guesses of the winer
    def show_guesses_winer(self, iterable):
        print("These were your guesses:", end=" ")
        for guess in iterable:
            print(guess, end=" ")
        print()

    #This block of code ask the player if they want to play again or not
    def ask_play_again(self):
        answer_player= input('Do you want to play again? ')
        if answer_player.lower() in ["yes", "y", "si", "s"]:
           return True
        else: 
            print('See you later')
            print()
            return False

class Player: #class responsible for managing the player operations

    # This function get the player guess from the input
    def get_guess_player(self):
        time.sleep(2)
        number= int(input("I'ts your turn, please guess the number, write it down here:"))
        return number
    
    # Here I'm going to evaluate the new range of minimum and maximum so that the computer's guesses are smarter,
    # considering the guesses of the user and computer
    def create_new_range_for_guesses(self, number):
        global minimo
        global maximo
        if number < secretNumber:
            if number > minimo:
                minimo= number
        
        else:
            if number < maximo:
                maximo=number
        
    
class Computer(Player): #class responsible for managing the player operations, inhering a method from Player.

    # This function get the computer guess from the random method
    def get_guess_computer(self, min, max):
      time.sleep(2)
      computerNumber= random.randint(min, max)
      return computerNumber
    
# I create the instances for my three classes
game= Game()
player= Player()
computer= Computer()

# This is the principal function, which is in charge to execute the loop for the game 
def mainFunction(): 
    game.start()  
    #Create two empty list which I will use in the main function
    global guesses_computer, guesses_player
    global minimo, maximo
        
    guesses_computer= []
    guesses_player= [] 
    flag_for_break_loop= True

    while flag_for_break_loop:
        print("##### Player's turn ####")
        player_guess= player.get_guess_player()
        guesses_player.append(player_guess)
        player.create_new_range_for_guesses(player_guess)
        time.sleep(2)
        if game.evaluate_guess(player_guess, secretNumber):
            flag_for_break_loop= False
            game.show_guesses_winer(guesses_player)
            break
        
        print("#### Computer's turn ####")
        computer_guess= computer.get_guess_computer(minimo, maximo)
        print(f"It's the computer's turn: {computer_guess} ")
        guesses_computer.append(computer_guess)
        computer.create_new_range_for_guesses(computer_guess)
        time.sleep(2)
        if game.evaluate_guess(computer_guess, secretNumber):
            flag_for_break_loop= False
            game.show_guesses_winer(guesses_computer)
            break

    minimo= 1
    maximo= 100
    guesses_computer= []
    guesses_player= []
     #This return will be used in my test     
    return flag_for_break_loop

     
if __name__ == '__main__':
    game = Game()
    while True:
        mainFunction()
        if not game.ask_play_again():
            break
