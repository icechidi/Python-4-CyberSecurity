num = 0
list1 = [0]
for list in list1:
    num = int(input("Enter a list of numbers: "))
    if num != -99:
        list1.append(num) 
    else:
        break
    
for i in list1:
    print(i)