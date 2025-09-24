# Functions:
# A functions is a block of codethat performs a specific task.
#syntax:
# def function_name(parameters):
#     function body code
#     return value # optional
# function_name()
#example:
# def greet():
#     print("Hello World")
#calling a function :
#calling a function means telling python to run the code inside a function by it's name followed by paranthese()
# def greet(): #function name 
#      print("Hello world")
# greet()  # calling a function.


# def greet(Name ,Branch):  #function name 
#     print("Hello", Name ,Branch)
# greet("Harshitha","CSM") # calling a function.
# greet("Harshitha","CSM")
# greet("Harshitha","CSM")

# passing parameters & arguments.
# prameters: 
# a variable declared inside the function defination .
# its acts as an empty container waiting to recieve a value

#Argument:
# the actual value we pass into the function when calling it.
# it fills the empty container(parameter).
# Example:
# def greet(Name,RollNo):
#      print("Hello",Name,"your RollNo is" , RollNo)
# greet("Harshitha","N3")

# #same task without function.
# name = "Harshitha"  # here name is input variabe(parameter), and "Hartshitha" is value to the parameter(Argument)
# print("Hello", name)

# # types of Functions Arguments:
# # A. positional arguments:
# # when we pass arguments in the same order as the function parameter, they are called positional arguments.
# #here the order (position) is very important.
# def greet(rollno, name):
#      print("Hello",name,"your rollno is" ,rollno) #step 3 execute the line
# greet("N3","Harshitha") #Step1: function calling

# # B. Keyword Aguments: 
# #  when we pass values or arguments by writing the parameter(variable = value), they are called as keyword arguments.
# def greet(rollno, name):
#      print("Hello",name,"your rollno is" ,rollno) 
# greet(name="Harshitha",rollno="N3")

# # C. Default argument:
# # when a parameter has default value (assigning the value in parameter) in the function defination, it becomes a default argument. 
# def greet(name = "student"):
#      print("Hello",name)
# greet()
# greet(name="Sushmitha")

# # D. variable length Arguments:
# # sometimes we dont know how many arguments will be passed to a function .
# # 1. "args":(variable length Arguments):
# # Collects multiple values into a tuple.
# # L = 10,20,30,40,50
# def sum1(*List1):
#      sum2 = 0
#      for i in range(len(List1)):
#           sum2 = sum2 + List1[i]
#      print (sum2)
#      print (type(List1))
# sum1(10,20,30,40,50)

# # 2. **kwargs:(keyword variable-length arguments)
# # collects multiple key=value pair into a dictionary.
# def details(**info):
#      for i,j in info.items():
#           print(i,":",j)
# details(Name= "Harshitha",Rollno="N3",Branch= "CSM")

# Scope of the variable:
x = 10 # Global variable
def var1():
     y=5 # local variable
     print("inside var1 func tion", x,y)
# var1()
# def var2():
#      print("inside var 2 function", x,y)
# var2()
# def var2():
#      print("outside function ",x,y)
