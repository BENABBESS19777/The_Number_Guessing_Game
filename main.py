###### The Number Guessing Game ######
import random
from art import logo

def start_game():
    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a number between 1 and 100")

def generate_number():
    return random.randint(1, 100)

def guessed_number():
    print(logo)
    Guessed_Number = generate_number()
    difficult_type = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficult_type == "easy":
        Attempt_Number = 10
    else:
        Attempt_Number = 5
    End_Game = True
    while End_Game:
        Guessed_Check = int(input("Make a guess: "))
        if Guessed_Check == Guessed_Number:
            print ( f"Yay, you have guessed the number {Guessed_Number} ")
            End_Game = False
        elif Guessed_Check > Guessed_Number:
            print("Too high")
            Attempt_Number -= 1
            print(f"you have {Attempt_Number} attempts remaining to guess the number")
            print(Guessed_Check)
            if Attempt_Number == 0:
                print(f"Game Over, the number was {Guessed_Number}")
                End_Game = False
            else: 
                End_Game = True  
        else :
            print("Too low")
            Attempt_Number -= 1
            print(f"you have {Attempt_Number} attempts remaining to guess the number")
            print(Guessed_Check)
            if Attempt_Number == 0:
                print(f"Game Over, the number was {Guessed_Number}")
                End_Game = False
            else: 
                End_Game = True    

guessed_number()


  