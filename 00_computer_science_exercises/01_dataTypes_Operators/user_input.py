#User Input Pratice, Tyshawn Ricks, v0.0

# input() is the built in function to get information from the KEYBOARD.
# BASIC EXAMPLE
variableName = input("Please type a variable name and press enter\n.")
print(variableName)

# input() saves ALL INPUT TO STRING DATTA TYPES BY DEFAULT!!!!
# input() saves ALL INPUT TO STRING DATTA TYPES BY DEFAULT!!!!
# input() saves ALL INPUT TO STRING DATTA TYPES BY DEFAULT!!!!
# input() saves ALL INPUT TO STRING DATTA TYPES BY DEFAULT!!!!

# INCORRECT, CAUSES A CONCATENATION ERROR.
# myNumber = input("Please type an INTEGER number and press enter.\n")
# print(myNumber + 5)

# Correct -- Use a wrapper.
myNumber = int(input("Please enter an INTEGER number and press enter,\n"))
#print(myNumber + 5)

# Wrapper Funcions
# int() will convert the data to a INTEGER if possible.
newNumber = input("Please type a value and press enter.\n")
print(int(newNumber)) # can convert STRING to INTEGER.
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # can convert INTEGER to STRING.

# Float() will convert the data to a FLOAT if possible.
newNumber = input("Please type a value and press enter.\n")
#print(int(newNumber)) <-- cannot convert FLOAT to INTEGER 
print(float(newNumber)) # can conert STRING to FLOAT.
print(str(newNumber)) # can convert FLOAT to STRING.
# str() will convert the data to a STRING if possible.
newNumber = 5
print(newNumber + newNumber) # Should print 10
print(str(newNumber + newNumber)) # Should print 55
