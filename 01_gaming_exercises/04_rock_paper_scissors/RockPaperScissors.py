# Rock, Paper, Scissors by Tyshawn Ricks, v0.1

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
isCorrect = input("is that correct? Type yes or no and press enter.\n")
if isCorrect == "yes".lower():
    print(f"Ok {playerChoice}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Please type you name and press enter.\n")





# The rules
print("""
Welcome to the Rock, paper, scissor robot!
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
        




    # print the current score 
    # let player select rock, paper, scissor
    # let cpu select choice at random
    # compare player choice to cpu choice
    # print the results to the screen
    # award point to the winner and output results
