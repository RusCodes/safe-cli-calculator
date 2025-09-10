total = 0
count = 0
average = 0
num = None
while num != "done" :
    num = input("Enter a number: ")
    try :
        fNum = float(num)
        count = count + 1
        total = total + fNum
        average = total / count
    except :
        print ("Invalid Input")
        continue


print("all done")
print("Sum:", total, "count:", count ,"Average:", average)