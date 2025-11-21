
numOne = int(input("Enter num 1: "))
numTwo = int(input("Enter num 2: "))
numThree = int(input("Enter num 3: "))

if numOne >= numTwo:
    if numOne >= numThree:
        print("Num one is the greatest")
    else:
        print("Num 3 is the greatest")

else:
    if(numTwo > numThree):
        print("Num 2 is the greatest")
    else:
        print ("Num 3 is the greatest")