# known variable

speed=340

# user input other variable

time=int(input("How many seconds was it after the flash of lightning that you heard the thunder in seconds "))

# process

distance = time*speed
km = distance/1000
miles = km/1.609

# display to user

print("The distance in km ",(km))
print("The distance in miles ",round(miles, 2))     #USEFUL, ROUND limits decimal points