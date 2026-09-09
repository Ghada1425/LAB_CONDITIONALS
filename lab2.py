 
weight=float(input("Enter your weight: "))
height=float(input("Enter your height: "))  
bmi = weight / (height * height)
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight fit and healthy.")
else:
    print("You are overweight.")