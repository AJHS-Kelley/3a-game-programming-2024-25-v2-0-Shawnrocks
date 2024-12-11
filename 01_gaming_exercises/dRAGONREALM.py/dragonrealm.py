# Dragon Realm, <STUDENT_NAME>, v0.0 <-- Update this information. 
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# Almost no new code added. 
# Missing the file saving code. 
# You need to finish by Friday. 
# 2024-12-09 -- No new code added. 50%.  Finish and resubmit by 2024-12-16 @ 3:00PM 

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

    hasTorch = input("Do you wish to pick up this torch? Yes or No")
    if hasTorch == "yes":
        print("You have picked up the torch")

    safeCave = False
    if hasTorch == "yes":
        safeCave == True
        
    if hasTorch == "yes":
        print("You enter this dark and void space with no light how do you wish to go")
        time.sleep(2)
        print("You hear something creeping up on you")
        time.sleep(2)
        print("What do you wish to do?\nHide?\nRun?\nApproach?")
        run = input("Do you wish to run away?\n Yes or No").lower
        if run == "yes":
            print("you managed to escape from the mysterious being but trip due to having no light")
        else:
            print("You hear it get closer")
            time.sleep(2) 
            print("Its getting closer and closer")
            time.sleep(2)
            print("you feel it breathing on your skin")
            time.sleep(3)
            print("It pushes you back and...")
            alive = random.randint(1, 2)
            if alive == 1:
                print("spares you")
            else:
                print("Ends you off")        
        
    

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    
