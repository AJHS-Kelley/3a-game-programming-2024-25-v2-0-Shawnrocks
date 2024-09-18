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
if isCorrect == "yes":
    print(f"Ok {playerChoice}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Please type you name and press enter.\n")
