
ageRange = int(input("Enter your age to check if you're eligible to vote: "))

if ageRange >= 18:
    print("You are Eligible to vote")

elif ageRange <=0:
    print("Enter a valid Age range")

else:
    print("Not Eligible to vote")