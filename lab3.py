x=int (input("what is the product of 7 and 24?"))
if x == 168:
    print("Correct!")
else:
    print("Incorrect.try again.")
    while x != 168:
        x=int (input("what is the product of 7 and 24?"))
        if x == 168:
            print("Correct!")
        else:
            print("Incorrect.try again.")