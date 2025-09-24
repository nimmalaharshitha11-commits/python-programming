#Sets:
#set is a collection data type which is used to store multiple values in a single variable.
# syntax:
# My_set = {element1,element2,element3}


# Charecteristics of sets:
# unordered:
# example: {1,2,3} and {3,2,1} are considered same set.
# unindexed: You cannot access set elements by the index like lists or tuples.set[1]
# a = {1,2,3}
# print(a[1])
# Unique values only: Duplicate values are automatically removed from the set 
# a = {1,2,3,3,2,1,1,1,2}
# print(a)  #output {1,2,3}
# Creating a set :
# s1 = {1,2,3}
# s2 = {10,12,5,"Hello", True}
# Empty set :
# s31 = {}
# s3 = set ()
# print(type(s3))  #set

# #Accessing sets:
# #we cannot directly access an element using index but we access an element using loops.
# A = {"Rajinikanth","snake king","upendra"}
# for role in A:
#     print(role)
# Adding an element in sets:
# S = {12,18,20}
# S.add(25) # add any single element in any position
# S.update([34,29])
# print(S)

# #deleting the element in sets:
# S = {34,12,18,20,25,29,25}
# S.remove(25)
# print(S)

#discards():
# s = {34,12,18,20,25,29,25}
# s.discard(25)
# print(s)
# #clear(): removes the every element from the set.
# s = {34,12,18,20,25,29,25}
# s.clear()
# print(s)
# #pop(): removes the random element from the set.
# s = {34,12,18,20,25,29,25}
# s.pop()
# print(s)
# Mathematical operatorsin set:
#union "U"="|": prints the all unique values or element from the both sets.
# a = {1,2,3}
# b = {4,5,6}
# print(A|B) # {1,2,3,4,5,6}

#Intersection "n" = "&" :
# a = {1,2,3}
# b = {4,5,6}
# print(a & b) # {1,2,3,4,5,6}

# # Mathematical operations using functions:
# A = {1,2,3,4}
# B = {3,4,5,6}
# # Union
# print(A.union(B)) #(1,2,3,4,5,6)
# # Intersection 
# print(A.intersection(B)) #(3,4)
# # Difference
# print(A.difference(B))  #(1,2)
# # symmetric difference
# print("A.symmetric difference(B)") #(1,2,5,6)
# Sum () : |
s = {10,15,82,96,22}
print (sum(s))
#len():
print(len(s))
# max:
print(max(s))
#min():
print(min(s))
