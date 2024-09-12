# Awarding Extra Lives, Tyshawn Ricks. v0.0


lives = 3
score = int(input("Please Enter Score\n"))
#Allow the user to input the score

# If score is 10000 or less
    # Lose a life
# If score is > 10000 but less than 100001
    # Give 1 extra life
#If score is > 100000
    #Give 2 extra lives

# Output the score and number of lives to the screen.


if score >= 100000:   
    print("You receive 2 extra lives.\n")
elif score >= 10000:
    print("You recieve 1 extra life.\n")
else:
    print("You lose a life.\n")



