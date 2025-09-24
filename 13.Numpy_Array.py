#numpy:
#numpy(Numerical Python) is a python library used for scientific and mathematical computing.

#Importing the numpy in library.
import numpy as np

#creating an array with numpy :
# 1D Array :
A1D = np.array([1,2,3,4,5])
# print(A1D)
# 2D Array :
A2D = np.array ([[1,2,3],[4,5,6],[7,8,9]])
 
#[
#   1  2  3
#   4  5  6  
#   7  8  9
#  ] 
#print(A2D)

# #methods & operations in numpy arrays :
# #1. Basic array information methopd:
# A = np.array([1,2,3,4,5])
# #ndim : Returns the number od dimensions of the arrays .
# print(A.ndim)   #1
# print(A2D.ndim)  #1
# #shape : Returns a tuple showing the sizes of the array in each dimentions(rows,colums,etc..)
# print(A2D.shape)  #(3,3)
# #size:Returns the total number of elements in the array.
# print(A2D.size)   #len = 9
# #dtype: Returns the datatype of the elements in the array.
# print (A2D.dtype)   #= type = int64

# #Creating an array with numpy:
# # zeros: creates an array of 6 zeros.
# print(np.zeros(6))
# #ones : Creates an array of 6 ones.
# print(np.ones(12))

# #arange:
# print(np.arange(1,11,1))
# print(np.arange(0,11,2))
# print(np.arange(1,11,2))

# #linspace: crteates 3 numbers evenly spaced between 0 and 1
# print(np.linspace(0,1,3))

#Mathematical operations:
# A = np.array([1,2,3,4,5])
# L = [1,2,3,4,5]
# print(A+6)
# print(A-1)
# print(A*2)
# print(A/2)
# print(A//2)
# print(A**2)

#Aggregate functions:
# A = np.array([1,2,3,4,5])
# #sum():
# print(np.sum(A))
# #mean():
# print(np.mean(A))
# #max():
# print(np.max(A))
# #min():
# print(np.min(A))
# #median():
# print(np.median(A))
# #std:
# print(np.std(A))
# #cumprod:
# print(np.cumprod(A))

#Matrix operations:
Mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
Mat2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
# [
#     9 8 7
#     6 5 4
#     3 2 1
# ]
print(Mat1+Mat2)
print(Mat1**2 )
print(Mat1*Mat2)

#dot():
print(np.dot(Mat1,Mat2))
#Transpose:
print(np.transpose(Mat1))
