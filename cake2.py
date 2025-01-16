#variables for price

cupcakeprice = 40
macaronprice = 50
cheesecakeprice = 70

#inputs from user

cupcakes = int(input("How many cupcakes do you plan to sell "))
macaron = int(input("How many macarons do you plan to sell "))
cheesecake = int(input("How many cheesecakes do you plan to sell "))

#process

totalcup=cupcakeprice*cupcakes
totalmac=macaronprice*macaron
totalcheese=cheesecakeprice*cheesecake
totalmoney=(totalcup+totalmac+totalcheese)/10

print("You will make £",(totalmoney))