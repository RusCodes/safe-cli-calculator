##Program that uses input
#name = input("Enter your name: ")
#print (name)

#program 2
try: 
    hours = input("Enter hours: ")
    rate = input("Enter rate: ")
    fRate = float(rate)
    fHours = float(hours)
except: 
    print ("Error please input digits")
    quit()


pay = fRate * fHours
print ("Pay is:", pay)
#


