# Error Handling:
# Types of exeption in python:
#1. Zero Division Error:
# try:
#     a= int(input("Enter the numerator: "))
#     b= int(input("Enter the denominator: "))
#     c= a/b
#     print(c)
# except ZeroDivisionError:
#     print("the values given is invalid because dinominator should not be zero")
# try:
#     a= int(input("Enter the numerator: "))
#     b= int(input("Enter the denominator: "))
#     c= a//b
#     print(c)
# except ZeroDivisionError:
#     print("the values given is invalid because dinominator should not be zero")
# try:
#     i = 3
#     n = int(input("enter the n value: "))
#     if i%n == 0:
#         print("yes, number is multiple of ", n)
#     else:
#         print("no, number not is multiple of", n)
# except ZeroDivisionError:
#     print("error: division by zero is not possible")

# 2. Value Error:
try:
    rollno = int(input("enter your rollno: "))
except ValueError:
    print("error: given value is not in the integer datatype.")

# 3. Index Error:
 
