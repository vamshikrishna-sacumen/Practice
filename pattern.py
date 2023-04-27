# initialising user input for number
num=int(input("Enter Number:"))

# looping num
for row in range(num):
    for col in range(num):
        if row>=col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


