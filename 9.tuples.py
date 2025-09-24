#tuples is a collection data types, which is used to store multiple values in a single variable.
# coordinates = ("x","y")
# My_tuple = (10,20,30)
# print(My_tuple)
# print(type(My_tuple))

#creating a tuple:
#empty tuple
# Et = ()
# #tuple with numbers:
# N = (1,2,3,4,5,6,7,8)
# #tuple with strings:
# S = ("A","B","C","a","b","c")
# #tuple with mixed datatypes:
# M = (24,3,14,"a","c",True,False)
# #tuple with single element:
# a = 10 #int
# print(type(a))
# b = [10] # list
# print(type(b))
# c = (10,) #tuple
# print(type(c))
#accessing elements:
#tuples uses index values to access an element
a = (10,20,30,40)
#i =  0  1  2  3
# print(a[0])#10
# print(a[1])#20
# print(a[2])#30
# print(a[3])#40

# print(a[-1])#40
# print(a[-2])#30
# print(a[-3])#20
# print(a[-4])#10

#slicing the tuple:
#extracts part of the tuple using start index and end index
#([start index: end index])
#in tuple it will print before the end index value.
A = (10,20,30,40)
#i =  0  1  2  3
#-i= -4 -3 -2 -1 
# print(A[1:3]) # 20,30
# print(A[:2])  # 10,20
# print(A[-3:-1])# 20,30

#changing the values:
#tuples are inmutable so we cannot change the values
A[1] = 50
print(A) #TypeError: 'tuple' object does not support item assignment
#append():
A.append(50)
print(A)

# length:
# max:
# min:
# sum:
# concatenation
# repetation

# searching and checking:
# in operator:
# not in operator:
# index():
# count():
#sorting and reversing 
