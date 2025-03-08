#the program that calculates inverse of a 2x2 matrix (the formulas are taken from the book of Diesenroth - Mathematics for Machine Learning)
import numpy as np #numpy for the matrix operations

mtrx=np.random.randint(0,10, size=(2,2)) #assigning random values to the matrix' elements
#mtrx=np.zeros((2,2)) #uncomment if you want to see how it works with 0 determinant
#[a b]
#[c d]
a=mtrx[0,0] #another names for the matrix' variables, for convenience
b=mtrx[0,1]
c=mtrx[1,0]
d=mtrx[1,1]
#calculation
determinant=(a*d)-(b*c) #determinant, that is the part of the formula of 2x2 matrix' inverse
mtrx_prime=np.array([[d,-b],[-c,a]]) #in the math book it's called A', and idk what it is. It's not a transpose, afaik
#output
if determinant!=0: #can calculate the inverse only if determinant!=0
    mtrx_inv=(1/determinant)*mtrx_prime #the formula for the inverse
    print (f"Initial matrix:\n{mtrx}\nDeterminant:\n{determinant}\nA':\n{mtrx_prime}\nInverse:\n{mtrx_inv}\nInitial matrix*inverse (identity matrix):\n{mtrx@mtrx_inv}")
else:
    print(f"Initial matrix:\n{mtrx}\nDeterminant:\n{determinant}")
    print("The determinant=0, the matrix is noninvertible/singular") #if determinant is 0, the inverse doesn't exist
    
#OUTPUT (determinant!=0):
# Initial matrix:
# [[4 0]
#  [8 5]]
# Determinant:
# 20
# A':
# [[ 5  0]
#  [-8  4]]
# Inverse:
# [[ 0.25  0.  ]
#  [-0.4   0.2 ]]
# Initial matrix*inverse (identity matrix):
# [[1. 0.]
#  [0. 1.]]

#OUTPUT (determinant=0):
# Initial matrix:
# [[0. 0.]
#  [0. 0.]]
# Determinant:
# 0.0
# The determinant=0, the matrix is noninvertible/singular
