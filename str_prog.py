# creating str accepting user input

str1=input("Enter string:")

# defining empty str

str2=""

# performing swapcase of str without using builtin method

for i in str1:
    if "A" <= i <= "Z":
        str2 += chr(ord(i)+32)
    if "a" <= i <= "z":
        str2 += chr(ord(i)-32)
    else:
        pass
print(str2)