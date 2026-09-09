
while True:
    number = int(input("Enter a number: "))
if number < 1:
    print("Please enter a number greater than 0.")
    for i in range(1, number + 1):
        print(i)
    