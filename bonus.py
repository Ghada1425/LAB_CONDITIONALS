
number=int(input("Enter a number: "))
calculations=0
evennumber=0
for i in range(1,number + 1):
    calculations += i
    if i % 2 == 0:
        evennumber += i
print("The sum of all even numbers from 1 to", number, "is:", evennumber)
