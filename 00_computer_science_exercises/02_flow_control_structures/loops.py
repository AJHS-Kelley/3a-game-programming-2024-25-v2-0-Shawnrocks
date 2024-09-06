#loops, Tyshawn Ricks, v0.0

# TWO TYPES OF LOOPS
# for <-- Used when you know how many loops you'll need.
# While <-- Used when you do not know how many loops you'll need.

# for loop is like Go Fish, you search each card for what the player asked.
# While loop is like musical chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOOP IS CALLED AN iteration
# "iterate through the list" means use for loop

# for loop example -- Iterating a list
# fruits = ["apple", "banana", "strawberry", "tomato"]
# for eachFruit in fruits:
#     print(eachFruit)

# continue Keyword -- skips the current iteration and then finishes the loop.
fruits = ["apple", "banana", "strawberry", "tomato"]
for eachFruit in fruits:
    print(eachFruit)
    if eachFruit == "banana":
        continue
    print(eachFruit)
    # break Keyword -- Immediaetly exit the loop
fruits = ["apple", "banana", "strawberry", "tomato"]
for eachFruit in fruits:
    print(eachFruit)
    if eachFruit == "banana":
        break
    print(eachFruit)