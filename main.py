###### The Number Guessing Game ######
import random
from art import logo

def start_game():
    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a number between 1 and 100")

def generate_number():
    return random.randint(1, 100)

start_game()
Guessed_Number = generate_number()
print(Guessed_Number)