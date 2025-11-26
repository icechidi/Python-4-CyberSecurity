
leapYear = int(input("Enter a number to check if LeapYear: "))

if (leapYear % 100 != 0 and leapYear % 4 == 0) or (leapYear % 400 == 0):
    print("You entered a leapYear")
else:
    print("It's not a leapYear")