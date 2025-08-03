import random

choices = ["rock" , "scissor" , "paper"]
while True:
    player = input("Player 1 enter your choice or finish with done a game:").lower()
    
    if player == "done":
        print("Game ended. Thanks for Playing")
        break
    
    if player not in choices:
        print("Error you entered an invalid choice try again")
        continue
    
    computer = random.choice(choices)
    print(f"Computer chose {computer}")
    
    
    if player == computer:
        print("Its tie no one win")
    elif player == "rock" and computer == "scissor":
        print("You win")
    elif player == "scissor" and computer == "paper":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    else:
        print("Computer Win")
