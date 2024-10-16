# Rock, Paper, Scissors by Tyshawn Ricks, v0.3

# Module Imports
import random, time

# DATA STRUCTURES -- player
playerScore = 0
playerChoice = None 
numDraws = 0

# Data Structures -- CPU
cpuScore = 0
cpuChoice = None

#Main game loop
loopCount = 0
loopsReq = int(input("How many loops do you want?\nEnter an integer, no commas, and press ENTER.\n"))
# req is the universal abbreveation 
rpsTimeStart = time.time() # Returns the number of seconds since Jan 01. 1970 @ 12:00 AM
while loopCount < loopsReq:


    cpuChoice = random.randint(0,2) # randomly select 0, 1, or 2
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice = "paper"
    elif cpuChoice == 2:
        cpuChoice = "scissor"
    else:
        print("Bro broke the game.\n")
        exit()

        # compare player choice to cpu choice

        # print the results to the screen
    playerChoice = random.randint(0,2) # randomly select 0, 1, or 2
    if playerChoice == 0:
        playerChoice = "rock"
    elif playerChoice == 1:
        playerChoice = "paper"
    elif playerChoice == 2:
        playerChoice = "scissor"
    else:
        print("Bro broke the game.\n")
        exit()
    

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

print(f"Your Final Score: {playerScore}\n CPU Final Score: {cpuScore}\n")
if playerScore > cpuScore:
    print(f"Congratulations, you won\n")
elif cpuScore > playerScore:
    print(f"The CPU wins. You get better")
else:
    print("Error")
    exit()

loopCount += 1











rpsTimeStart = time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"Number of loops: {loopCount}\n")
print(f"Execution Time {rpsTime: .2f}")

    # award point to the winner and output results
# print the current score 
    # let player select rock, paper, scissor
    # let cpu select choice at random