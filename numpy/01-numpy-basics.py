from cmath import pi
import numpy as np

# Note that numpy.array is not the same as the Standard Python Library class array.array,
a = np.arange(15).reshape(3,5)
print(a)

# reshpae( y, x ) => reshape array to array that has y rows and x columns.
#  [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]

# ndarray.shape : get demensions of the array.
print(a.shape)
# ( 3, 5 )

# number of demension.
print( a.ndim )
# 2

# element type.
print ( a.dtype.name )
# 'int32'

# itemsize : each element byte size.
print ( a.itemsize )
# 4

# element count 
print ( a.size )
# 15

# Array Creation
a = np.array([2,3,4])
print(f'{a=}')

# WRONG Example
# a = np.array(2,3,4) => if argument is not list, it makes error.

# fill zero
a = np.zeros((3,4))
print ( f'np.zeros = {a=}')

# arange example
a = np.arange(10,30,5)
# 10, 15, 20, 25

a = np.arange(0,2,0.3)
# 0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8

# linspace example
a = np.linspace(0, 2, 9)
# 0, 0.25, 5, 0.75, 1. , .125, 1.5, 1.75, 2.

a = np.linspace(0, 2 * pi, 100)
f = np.sin(a)

# set printoption.
import sys
np.set_printoptions(threshold=sys.maxsize)  # sys module should be imported
print ( np.arange(10000) )


# Basic operaotor
a = np.array([20,30,40,50])
b = np.arange(4)
c = a - b 
# [20,29,38,47]

b**2
# [0,1,4,9]

10 * np.sin(a)
# [ 9.12945251, -9.88031624,  7.4511316 , -2.62374854]

a < 35
# [True, True, False, False]

A = np.array([[1,1], [0,1]])
B = np.array([[2,0], [3,4]])

A * B
# elementiwse product 
# element끼리 곱함.
# [2,0], [0,4]

A @ B
# matrix product
A.dot(B)
# Another matrix product
# result : [5,4], [3,4]