# Path = C:/Users/Karan/OneDrive/Documents/whitehatjr/python/C97/projectPost/
# - Open the terminal 
# - Using cd command go to the folder which contains your guessingGame.py file 
# - To run the file we use python3 filename command.
#  Here we'll write =====* python3 guessingGame.py * ==== We'll see output on the terminal
import random
print("Number guessing game")
number = random.randint(1, 9)
chances = 0
print("Guess a number (between 1 and 9):")
while chances < 5:
    guess = int(input("Enter your guess:- "))
    if guess == number:
        print("Congratulation YOU WON!!!")
        break
    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)
        chances += 1
    else:
        print("Your guess was too high: Guess a number lower than", guess)
        chances += 1
if not chances < 5:
    print("YOU LOSE!!! The number is", number)