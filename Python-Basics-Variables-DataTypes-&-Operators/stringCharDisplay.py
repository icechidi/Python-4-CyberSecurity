text = input("Enter a String: ")

if len(text)>0 and len(text) != "":
    print("First Character of string ", text[0])
    print("Last Character of string ", text[-1])
    
else:
    print("Enter a valid string")