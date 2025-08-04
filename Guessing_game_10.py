# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they
# guessed too low, too high, or exactly right. (Hint: remember 
# to use the user input lessons from the very first exercise)
import random

random_number = random.randint(1 , 10)
while True:
    
    userInput = input("Enter a number to be guess :")

    if userInput.lower() == "done":
        print("Game ended. Thanks for playing")
        break
    userInput = int(userInput)
    if userInput == random_number:
        print("You guess a correct number congrats")
    elif userInput > random_number:
        print("You entered number greater than a number to be guessed")
    elif userInput < random_number:
        print("You entered a number less than the number to be guessed")
    else:
        print("You entered a number which is not in ranged")
        
print("Number to be guessed was :",random_number)