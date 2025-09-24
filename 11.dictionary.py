#dictionary
#dictionary is the in-built datatype, which is used to store multiple values in a single variabl.
#syntax:

#example:
# A = {"n":"Nandhan", "n":"Anurag"}
# print(A)
# #keys must be immutable :
# #keys can be(valid keys): integer,float,string
# My_dict = {
#     1:"value1",
#     10.2:"value2",
#     "key3":"value3",
#     "key4":"value4"
# # }
# print(My_dict)
# BioData = {
#     "Name":"Harshitha",
#     "Roll.No":"N3",
#     "Branch":"CSM",
#     "Place":"Medchal"
# }
# print(BioData)
# #Dictionary using constructer:
# BioData1= dict( Name="Harshitha", Roll_No="N3",Branch="CSM",Place="Medchal")
# #square brackets []:
# print(BioData["Name"])  
# print(BioData["Roll.No"])
# print(BioData["Branch"])
# print(BioData["Place"])

# #using get() mrthod:
# print(BioData.get("Name"))
# print(BioData.get("Roll.No"))
# print(BioData.get("Branch"))
# print(BioData.get("Place"))

# #adding and updating
# BioData["age"] = 17
# print(BioData)
# BioData["Place"] = "Dammaiguda"
# print(BioData)

#Removing in dictionary:
#pop(),popitem(),clear)()
# BioData = {
#     "Name":"sairam",
#     "Roll.No":"F9",
#     "Branch":"CSM",
#     "Place":"Charminar",
#     "Role":"Charminal_Modal"
# }
# print(BioData)
# #pop(): Removes the key value
# BioData.pop("Roll.No")
# print(BioData)
# BioData.pop("Role")
# print(BioData)
# #popitem:it removes the lats items from the dictionary 
# BioData.popitem
# print(BioData)
# #del(delete): deletes the keys from dictionary 
# del BioData ["Branch"]
# print(BioData)
# #clear():removes every item from the dictionary
# BioData.clear()
# print(BioData)
#updating update ():
# BioData.update({"Role":"web Developer","place":"Hyderabad"})
# print(BioData)

# BioData ={
#     "Name":"Sairam",
#     "Roll.No":"Fa",
#     "Branch":"CSM",
#     "Place":"Charminar",
#     "Role":"Software developer"
# }
# #keys(): it prints only the keys of dictionary
# print(BioData.keys())
# #values(): it prints only the values in dictionary
# print(BioData.values())
# #item(): it prints only key values in dictionary
# print(BioData.items())
# #loops of dictionary :
# # for i in BioData.values():
#     print(i)

#Nested tuple:
T = (10,(20,30),(40,50))
#i =  0    1       2
print(T[2][1])

#Nested Dictionary:
Students = {
    "S1":{"Name":"Harshitha","Roll.No":"N3"},
    "S2":{"Name":"Sushmitha","Roll.No":"N2"},
    "S3":{"Name":"Parvathi","Roll.No":"N1"}
}
print(Students["S1"]["Name"]),
print(Students["S2"]["Name"]),
print(Students["S3"]["Name"]),
print(Students["S1"]["Roll.No"]),
print(Students["S2"]["Roll.No"]),
print(Students["S3"]["Roll.No"])