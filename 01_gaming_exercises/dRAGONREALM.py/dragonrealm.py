# Dragon Realm, <STUDENT_NAME>, v0.0 <-- Update this information. 
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# Almost no new code added. 
# Missing the file saving code. 
# You need to finish by Friday. 


import random
import time
Axe = False
def displayIntro():

    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 4)
    
    if friendlyCave == 1:
        print("You lose lil bru")
    elif friendlyCave == 2:
        print("Hes still sleep bro")
    elif friendlyCave == 3:
        print("You got destroyed")
    elif friendlyCave == 4:
        print(f"do you wish to pick up {Axe}")
        


playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    
