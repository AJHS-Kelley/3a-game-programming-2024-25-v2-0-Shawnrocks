# Functions Pratice, Tyshawn Ricks, v0.0

import random

def helloWorldMulti(): # FUNCTION SIGNATURE
    """This function will output Hello, World! in a language the user chose. """ # DOCSTRING \
    # print a list of languages to the screen, at least three but no more than five.
    # allow the user to select (input) a choice for the language.
    # print "Hello, World!" to the screen in that language.

    print("""Hey, this will print which ever language shown below
        English
        Spanish
        Chinese\n""")

    language = input("Which of the languages above would you like\n").lower()

    if language == "english":
        print("Hello, World")
    elif language == "spanish":
        print("Hola, mundo")
    elif language == "chinese":
        print("世界您好")
    else:
        print("FAILURE")

helloWorldMulti() # FUNCTION CALL

# Function to determine even / odd numbers
argument1 = random.randint(-1000, 1000)

def isEven(argument1: int) -> bool: #Requires one argument (argument1) and RETURNS a boolean value
    """Determines if an integer value is even or odd."""
    if argument1 % 2 == 0:
        return True
    else:
        return False
    
print(isEven(argument1))

# Function with Multiple Arguments
def canRideRollerCoaster(age: int, height: int) -> bool:
    if age > 10 and height > 4:
        print("You can ride.\n")
        return True
    else:
        print("You cannot ride.\n")
        return False

canRideRollerCoaster(4, 10) # Arguments must be passed in the same order as the function signature indicates.