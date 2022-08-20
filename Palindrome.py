# #A palindrome is a number or a text that reads the same backwards or forwards.
# For example, each of the following five-digit integers is a palindrome:
# 12321,55555,4554,11611
# Write a program that reads in a five-digit integer and determines whether it is a palindrome



num = int(input("enter a 5 digit number"))
stringg = str(num)
k = len(stringg)
x = ""
if k == 5:

    for char in stringg:
        x = char + x
    if x == stringg:
        print("the number is a palindrome")
    else:
        print("this is not a palindrome")
else:
    print("this is not a 5 digit number")
print(x)