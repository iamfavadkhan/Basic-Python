# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations
# to the winner, and ask if the players want to start 
# a new game)

choice1 = "rock"
choice2 = "scissor"
choice3 = "paper"

while True:
    player1 = input("Player 1 enter your choice or finish with done a game:").lower()
    player2 = input("Player 2 enter your choice or finish with done a game:").lower()

    if player1 == "done" or player2 == "done":
        print("Game ended Thanks for playing")
        break
    if player1 == player2:
        print("Its a tie no win")
    elif player1 == "rock" and player2 == "scissor":
        print("Congrats Player1 Win")
    elif player1 == "scissor" and player2 == "paper":
        print("Congrats Player1 Win")
    elif player1 == "paper" and player2 == "rock":
        print("Congrats Player1 Win")
    elif player1 == "scissor" and player2 == "rock":
        print("Congrats Player2 Win")
    elif player1 == "paper" and player2 == "scissor":
        print("Congrats Player2 Win")
    elif player1 == "rock" and player2 == "paper":
        print("Congrats Player2 Win")
    else:
        print("Entered an Invalid Choices")
            
