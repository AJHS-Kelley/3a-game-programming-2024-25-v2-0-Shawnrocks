 # Data Types and Operators, Tyshawn Ricks, v0.0

 # Fundamental Data Types
 # String - str - Sequence of letters, numbers, spaces, or other characters.
 # Strings in python are inside ' ' or " "
 # idc if you use ' ' or " " long as you are consistent

 # boolean - bool - True or False values.

 # Float - float - any number with a decimal, +/-, including 0

 # Integers - int - any whole number, +/-, including 0.

 # Data types are stored in VARIABLES
 # A variable is basically a bucket with a name to put data into.
 # VARIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT
 # VARIABLES CANNOT START WITH A NUMBER
 # camelCaseVariableNames
 # snake_case_variable_names

 # DECLARING VARIABLES AND ASSIGNING VALUES

high_score = 238765 # int data type
highScore = 9764567 # int data types

carSpeed = 12.31 # float data type, miles per hour
car_speed = 3.14159 # float data type, miles per hour

hasAxe = True # boolean data type
isitPink = False # boolean data type

playerName = "Tyshawn Ricks" # string data type
enemyType = "fire" # string data type

 # ASSIGN NEW VALUES
playerName = "Goat Biscuit"
carSpeed = 2.3

 # DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 5.0

 # printing data types
newInt = 3
newFloat = 4.0
newString = "Skibidi Toilet"
newBool = False

print(type(newInt))
print(type(newFloat))
print(type(newString))
print(type(newBool))

 # printing Variables to Console/ screen 
print(playerName)
print(carSpeed)
print(isitPink)
print(enemyType)

 # printing variables and expressions to console/screen
print(car_speed + 5000000)
print(12 * 12)
print(car_speed)


 # PRINTING VARIABLES INSIDE STRINGS
print(f"Hello {playerName}. Your high score is {high_score}.\n")

 # ARITHMETIC OPERATORS
myInt = 3
myFloat = 2.57
myNum = 0

 # addition
myInt = 7 + 10
myFloat = 4.6 + 6.8

myInt = myInt + 5

myNum = myInt + myFloat 
 # when you add an int and a float together, the answer becomes a float

 # subtraction
myNum = myInt - myFloat
myInt = myFloat - 1.25

 # multiplication
myNum = myInt * myFloat

 # division
myNum = myInt / myFloat # first is numerator, second one is denominator

 # MODULUS (MODULO) % -- Returns REMAINDER after dividing.
 # MOST COMMMON USE FOR MODULUS IS DETERMINING EVEN / ODD NUMBERS
numStudents = 6
NumSlicesPizza = 35

leftovers = NumSlicesPizza % numStudents
print(leftovers)

 # EXPONENTS **
numSquared = 5**2 # 5 is the base, 2 is the exponent.

 # FLOOR DIVISION // -- divides, then rounds down to nearest int
myNum = myInt // myFloat

# Addition-Assignment Operator - Mostly used for counters
myNum = 5
myNum = myNum + 1 # Old School Method
myNum += 1 # New Hotness
myNum *= 1
myNum /= 1
 

#  # COMPARISON OPERATORS
 
#  # IS-EQUAL-TO == Are the two values equal to each other?
#  # Returns True or False based on evaluation.
# x = 12.0
# #print(x == 5)

#  # NOT-EQUAL-TO != Are the two values NOT equal?
#  # Returns True or False based on evaluation
# print(x != 12)
 
#  # GREATER THAN/ GREATER-THAN-OR-EQUAL TO
# print(5 > 3) # Greater Than
# print(12 >= 2) # Greater than or equal to

# # LESS THAN/ LESSS-THAN-OR-EQUAL TO
# print(5 < 3) # Less than
# print(12 <= 2) # Less than or equal to
  
# LOGICAL OPERATORS
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
age = 16
height = 75.0
eyeColor = "Brown"
 # In order to ride the Teacups, you must be at least 18 years old and 60" tall.
print(age >= 18 and height >= 60)
print(age >= 18 and height >= 60 and eyeColor == "Blue")
 # ALWAYS CHECK FOR THE LEAST-LIKELY TO BE FALSE CONDITION FIRST!!!!! 
#print(defeatedBoss == True and level > 5 and hasBlueKey == True)

 
 # or -- AT LEAST ONE CONDITOPM MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
print(age >= 18 or height >= 60)
print(age >= 18 or height >= 60 or eyeColor == "Blue")
 #ALWAYS CHECK FOR THE MOST-LIKELY TO BE TRUE CONDITION FIRST!!!!!
#print(defeatedBoss == True or level > 5 or hasBlueKey == True)
 
 # not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT.
a = 6
print(a == 6)
print(not(not (a == 6)))
 
 # COMBINING LOGICAL OPERATORS
#print(a == 6 and hasKey == True or isCloud == True)
#TRUE and 

 # IDENTIFY OPERATORS
g = 1.0
h = 1.0
i = g
print(g is h)
print(i is h)
print(i is not 1.0)
print(i is not g)

 # MEMBERSHIP OPERATORS
fruits = ["apple", "banana", "tomato"]
print("banana" in fruits)
print("potato" in fruits)