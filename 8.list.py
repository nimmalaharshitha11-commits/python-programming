# #        0, 1 ,2 ,3, 4
# list1 = (10,20,30,40,50)
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# #by negative values
# print(list1[-1])
# print(list1[-2])
# print(list1[-3])
# print(list1[-4])
# #slicing in list
# #slicing is tyaking out of a part from the main  list
# #slicing will extracts the post part or sublist using[start idx : end idx]
# #example:
# slc1 = ["prabhas","balayya","pspk","bob","bhai"]
# print(slc1[:3])
# print(slc1[:4])
# print(slc1[-3:])
# slc2 = ["hyd","mumbai","bengalure","canada","kerela"]
# print(slc2[-5:])
# print(slc2[2:])
# print(slc2[:3])
# KalkiCast =["prabhas", "kamal hasan","amitah bacchan","deepika pa","ssr"]
# KalkiCast.append ("deesha patani")
# print (KalkiCast)
# KalkiCast.insert(2,"vijay d")
# print(KalkiCast)
# KalkiCast.extend(["anudeep","mrunal thakur"])
# print(KalkiCast)
# KalkiCast.insert(5,"brahmanandam")
# print(KalkiCast)
# KalkiCast.remove ("mrunal thakur")
# print(KalkiCast)
# KalkiCast.pop(6)
# print(KalkiCast)
# KalkiCast[1] = ("sandeep reddy vanga")
# print(KalkiCast)
# #concatenation: joins the two lists together in one list
# #a=[1,2]
# #b=[3,4]
# #c=a+b
# #print(c)
# #repetition
# #a=[1,2]
# #n=int(input("enter the n value"))
# #b=a*n
# #print(b)

# #searching and checking
#  #in operator:
# # in operator is the membership operator which returns the true values when the values exists in the list
# a=[2,4,6,8,8,10,12,14]
# if 2 in a:
#     print("yes item is present in list")
# #not in operator:
# if 3 not in a:
#     print("3 not in a")
# print(a.index(8))
# print(a.count(8))
# #count
# a=[2,4,6,8,10,12,14,16]
# cnt = 0
# print(a.count(8))
# for i in range(10):
#     if i == 8:
#         cnt = cnt+1
# print(cnt)

# #sorting:
# st = [25,12,5,31,13,18,7,45,8,55,68]
# st.sort()
# print(st)
# st.reverse()
# print(st)
# st1 = [25,8,4,7,10]
# st1.sort(reverse = True)
# print(st1)
# frnd1= ["A","C","D","A","D","B","B","C","C","A","A"]
# frnd2= frnd1.copy()
# #frnd2[2] = "B"
# print(frnd2)
# #built in functions with loops
# print(sum(st))
# print(len(frnd1))
# print(max(st))
# print(min(st))
# #a= "hello world to the python programming"
# #b= a .split()
# #print(b)
# #multiple values using input data to the list
# #a = 10,20,30,40,50
# #a= int(input("enter the multiple value:")).split() # 10 20 30 40 50
# #print(a) 
# cars = ("thar","jaguar","audi","bmw")
# for car in cars:
#     print("cars=",car)
# #using index with for loop:
# a = len(cars)
# for i in range(0,a):
#     print("cars",i,cars[i])

# adding elements using for loop:
# list1 = []
# n = int(input("enter the number of list value: "))
# for i in range (0,n):
#     a = input("enter the list values: ")
#     list1.append(a)
# print(list1)
# # give the input values to the list from  0 to 10
# list2 = []
# n = int(input("enter the number of list value:")) #10
# if i in range(0,10): 
#     a = input("enter the list values")
#     list1.append(i)
# print(list1)
# list1 = []
# n = int(input("enter the number of list values:"))
# for i in range(a):
#     list1.append(i)
#     print(list1)

#sum of list items = 10 20 30 40 50 without usingsum()

# list1 = [10,20,30,40,50]
# sum = 0
# for i in list1:
#     sum = sum+i
# print(sum)
# sum = 1
# for i in list1:
#     sum = sum*i
# print(sum)
# #convert ["p","y","t","h","o","n"] to python
# list1 = ["p","y","t","h","o","n"]
# word = " "
# for i in list1:
#     word = word + i
# print(word)

# #find the maximum and minimum numbers from list without using max() and min()
# #with using max and min 
# list1 = [10,20,30,40,50]
# print(max(list1))
# print(min(list1))
# #without using max and min
# list1 = [6,46,2,87,5,54,9,75]
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1)
# print(len(list1))
# max1 = list1[0]
# min1 = list1[0]
# for num in list1:
#     if num > max:
#         max1 = num
#     if num < min:
#         min1 = num
# print(max1)
# print(min1)

#searching for an element in a list
# names = ["malla reddy sir", "revanth reddy sir","modi sir", "rahul sir"]
# searching_name = input ("enter the name to be found:")
# found = False
# for i in names:
#     if searching_name == i:
#         found = True

# if found:
#     print("yes")
# else:
#     print("no")

#count even and odd numbers 
# numbers = [7,10,12,17,18,23,31,45,227,229]

# evn_cnt = 0
# odd_cnt = 0

# for i in range(len(numbers)):
#     if numbers[i]%2 == 0:
#         evn_cnt += 1
#     else:
#         odd_cnt +=1
# print("number of even numbers are: ",evn_cnt)
# print("number of odd numbers are: ",odd_cnt)

#reversing a list without reverse
# list1 = [7,10,12,17,18,23,31,45,227,229]  # 1 = 10
# #ind  =  0  1  2  3  4  5  6  7  8   9
# l = len(list1)
# r_list = []
# for i in range(10-1,-1,-1):
#     r_list.append(list1[i])
# print(r_list)

#removing all negative numbers using loop # = (2,30,45,23,72,7)
# numbers = [-56,-9,2,-8,-30,30,45,23,-19,72,-55,-18,7]
# positive_list = []
# for i in range(len(numbers)):
#     if numbers[i] >=0:
#         positive_list.append(numbers[i])
        
# print(positive_list)

#multiply each element in the list
numbers = [56,92,8,30,30,45,23,19,72,55,18,7,0]
m = int(input("enter the number to be multiplied"))
After_multiplication  = []
for i in numbers:
    After_multiplication.append(i*m)
print(After_multiplication) 