# Dragon Realm, <STUDENT_NAME>, v0.0 <-- Update this information. 
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# Almost no new code added. 
# Missing the file saving code. 
# You need to finish by Friday. 
# 2024-12-09 -- No new code added. 50%.  Finish and resubmit by 2024-12-16 @ 3:00PM 
    
    
    
import random
import time

def gameOver(reason):
    "Handles game over and play again logic."
    print(f"\nGame Over: {reason}")
    play_again = input("Play again? (yes/no): ").lower()
    return play_again == "yes"

def encounterEnemy(enemy_name):
    "Handles combat with an enemy."
    while True:
        action = input(f"Do you fight the {enemy_name} or flee? (fight/flee): ").lower()
        if action == "fight":
            outcome = random.choice(["win", "lose"])
            if outcome == "win":
                print(f"You bravely defeat the {enemy_name}!")
                return True  
            else:
                print(f"The {enemy_name} defeats you.")
                return False  
        elif action == "flee":
            print(f"You narrowly escape the {enemy_name}, but you're still lost.")
            return True
        else:
            print("Invalid choice. Please enter 'fight' or 'flee'.")

def desertAdventure():
    "The desert adventure path."
    print("\nYou are in a scorching desert. The sun beats down mercilessly.")
    print("You see a shimmering oasis in the distance.")
    while True:
        action = input("Do you approach the oasis? (yes/no): ").lower()
        if action == "yes":
            print("You stumble upon the oasis. It's a mirage!")
            print("A giant Sandworm emerges from the sand!")
            return encounterEnemy("Sandworm") 
        elif action == "no":
            print("You wisely avoid the mirage and continue walking. You find a small, withered cactus.")
           
            return True 
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

def tundraAdventure():
    "The tundra adventure path."
    print("\nYou are in a freezing tundra. The wind howls fiercely.")
    print("You see a faint light in the distance.")
    while True:
        action = input("Do you approach the light? (yes/no): ").lower()
        if action == "yes":
            print("You find a small, abandoned cabin.")
            print("A Yeti bursts out of the cabin!")
            return encounterEnemy("Yeti") 
        elif action == "no":
            print("You decide to avoid the light and keep searching for shelter. You find a small cave.")
           
            return True 
        else:
            print("Error")

def game():
    "Main game function."
    playing = True
    while playing:
        print("\nWelcome to Choose Your Own Adventure!")
        while True: 
            choice = input("Where do you want to go? (desert/tundra): ").lower()
            if choice == "desert":
                player_survived = desertAdventure()
                break
            elif choice == "tundra":
                player_survived = tundraAdventure()
                break
            else:
                print("Error")

        if not player_survived: 
            playing = gameOver("You lost bro.")
        else:
            playing = gameOver("You survived... for now.") 


if __name__ == "__main__":
    game()
    
