#random time

import random

print("     #  ")
print("    #   ")
print("   ###  ")
print("  ######")
print("SORTING HAT")

name = str(input("What is your name? "))

number = random.randint(1,4)

print("You might belong in...")

if number==1:
    print("...Gryffindor")
elif number==2:
    print("...Slytherrin")
elif number==3:
    print("...Hufflepuff")
elif number==4:
    print("...Ravenclaw")