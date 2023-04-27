# initialising user input for number
num=int(input("Enter Number:"))

# looping num
for row in range(num):
    for col in range(num):
        print("*",end=" ") if row>=col else print(" ",end=" ")    
    print()


