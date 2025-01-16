print("Voting age checker")
age=int(input("What is your age? "))
years=(18-age)
if age>=18:
    print("You are eligible to vote")
else:
    print("You will be available to vote in "+str(years)+" years time")