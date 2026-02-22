# print("hellow sahiba")
# print("I started writing code in python ")
# n1=10
# n2=20
# print("sum of ", n1 ,"and ",n2 ," is " , n1 + n2)
# print("multiply with", n1," and", n2, " is " , n1 * n2)
# print("subtract  ",n1,"with", n2 ," is " , n1 - n2)

# function in the python
# def sum(a,b):
#     print(a + b)
# sum(30,20)

# Take input from the user like name and roll.
# a = input("enter your name")
# r = int(input("enter your name"))
# print("your name is",a)
# print("this is your roll",r)

#find greatest number in three nuber.   

print("Enter three numbers (unique, positive and not 0)")

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

# Check if all are positive and not zero
if (num1 <= 0 or num2 <= 0 or num3 <= 0):
    print("All numbers must be positive and not zero")

# Check if numbers are unique
elif (num1 == num2 or num2 == num3 or num1 == num3):
    print("Numbers must be unique")

# Find greatest number
elif (num1 > num2 and num1 > num3):
    print("Greatest number is", num1)

elif (num2 > num1 and num2 > num3):
    print("Greatest number is", num2)

else:
    print("Greatest number is", num3)