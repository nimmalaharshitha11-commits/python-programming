# # File = open("file name","mode") # r,w,a,rb,wb,r+,w+

# # file = open("student.txt ","w")
# # file.close()

# #types of read ():
# #1.read() =>
# file = open("student.txt","r")
# content = file.read()

# #2. readline() =>
# file = open("student.txt","r")
# content = file.readline() #1st line
# content = file.readline() #2nd line
# content2 = file.readline() #3rd line

file = open("student.txt","w")
# write, writeline
file.write ("Hello c++\n")
lines =["Hello nandhan\n","Hello Anurag\n","Hello world\n","Hello Python\n"]
file.writelines(lines)
file.close()
