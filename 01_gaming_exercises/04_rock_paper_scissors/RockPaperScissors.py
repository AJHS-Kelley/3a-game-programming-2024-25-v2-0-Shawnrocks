# Rock, Paper, Scissors by Tyshawn Ricks, v0.3

# Module Imports
import random

# DATA STRUCTURES -- player
playerScore = 0
playerName = "Test Player"
playerChoice = None 

# Data Structures -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Please type you name and press enter.\n")
print(f"Hello {playerName}!\n")
isCorrect = input("is that correct? Type yes or no and press enter.\n").lower

if isCorrect == "yes":
    print(f"Ok {playerName}, let's play rock, paper, scissors!\n")
else :
    playerName = input("Please Type your name and press enter.\n")




# The rules
print(f"""
Welcome, {playerName} to the Rock, paper, scissor robot!
it's time to play rock, paper, scissors
      
you will play against the CPU. The first player to score 5 points wins.
You will select from rock, paper, scissors!
The CPU will select rock, paper, scissors at random.
      
1) ROCK BEATS SCISSORS
2) SCISSOR BEATS PAPER
3) PAPER BEATS ROCK
""")     

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS
"""" YOu can put comments in these strings aswell """





#Main game loop
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points.\n")
    playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
        playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
        if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
            print("You are not following my rules. Please try again.\n")
            exit()
    print(f"You have chosen {playerChoice}\n")
else:
    print(f"You have chosen {playerChoice}\n")
    
    cpuChoice = random.randint(0,2) # randomly select 0, 1, or 2
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice == "paper"
    elif cpuChoice == 2:
        cpuChoice = "scissor"
    else:
        print("Bro broke the game.\n")
        exit()
    print(f"CPU Choice: {cpuChoice}")
        # compare player choice to cpu choice

        # print the results to the screen
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        #CPU WINS
    elif playerChoice == "rock" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
    #PLAYER wins
    elif playerChoice == "rock" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You both draw.\n")

    elif playerChoice == "scissors" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1

    elif playerChoice == "scissors" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1

    elif playerChoice == "scissors" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You both draw.\n")

    elif playerChoice == "paper" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You both draw.\n")

    elif playerChoice == "paper" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1

    elif playerChoice == "paper" and cpuChoice == "rock":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1








    # award point to the winner and output results
# print the current score 
    # let player select rock, paper, scissor
    # let cpu select choice at random