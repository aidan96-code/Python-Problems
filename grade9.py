print("Welcome to the grade checker")
mark=int(input("How many points did you get in the exam (0-60)? "))

if mark>60 or mark<0:
    print("Sorry this is not a valid score")
elif (mark>=54 and mark<=60):
    print("You achieved an A*")
elif (mark>=48 and mark<=53):
    print("You achieved an A*")
elif (mark>=42 and mark<=47):
    print("You achieved an A*")
elif (mark>=36 and mark<=41):
    print("You achieved an A*")
elif (mark>=30 and mark<=35):
    print("You achieved an A*")
elif (mark>=24 and mark<=29):
    print("You achieved an A*")
else:
    print("YOU FAILED")