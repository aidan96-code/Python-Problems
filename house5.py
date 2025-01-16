#storing the values of the house

streetname = "Edward Street"
typeofhouse = "tent"
numberofbedrooms = 12
price = 120000.99
frontgarden=True
garage=False
floors=5

#print the description with logic

print("A lovely",(typeofhouse),"situated on",(streetname),\
      "which comes with",(numberofbedrooms),"bedrooms with an asking price of £",round(price,2))

if frontgarden == True:
    print("This house also has a front garden")

if garage == True:
    print("This house comes with a garage")

if floors > 1:
    print("This house is multi-storey")
else:
    print("This house is a single floor")