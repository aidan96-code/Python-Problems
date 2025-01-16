#user input

print("###")
print("Hello, this will work out the price of your item after a sale")
print("###")
value= float(input("What is the value of your item? "))
discount = int(input("What is the percentage discount you are getting? "))

#process

saleprice = value-(value*discount/100)          #how to find discount

#end result

print("The reduced price is £",round(saleprice,2))