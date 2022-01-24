#using array module
#1-D arrays:
# 1. Printing the elements of an integer array / array traversal

from array import array

array1 = array('i', [10,20,30,40,50])
print("1. Printing the elements of an integer array / array traversal")
for x in array1:
   print(x)

#2. Printing the elements using index

from array import *

array1 = array('i', [10,20,30,40,50])
print("\n")
print("2. Printing the elements using index")
print (array1[0])
print (array1[1])
print (array1[2])
print (array1[3])
print (array1[4])

#3.array insertion

from array import *

array1 = array('i', [10,20,30,40,50])

array1.insert(1,60)
print("\n")
print("3.array insertion")
for x in array1:
   print(x)

#4. array deletion

from array import *

array1 = array('i', [10,20,30,40,50])

array1.remove(40)
print("\n")
print("4.array deletion")
for x in array1:
   print(x)

#5.array search
from array import *

array1 = array('i', [10,20,30,40,50])
print("\n")
print("5.array search")
print (array1.index(40))

#6. array update


array1 = array('i', [10,20,30,40,50])

array1[2] = 80
print("\n")
print("6.array update")
for x in array1:
   print(x)


#2. 2-D arrays

print("\n 2d arrays")
# 1.Accessing elements 
from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

print(T[0])

print(T[1][2])

for r in T:
   for c in r:
      print(c,end = " ")
   print()

#2.insert elements
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T.insert(2, [0,5,11,13,6])

for r in T:
   for c in r:
      print(c,end = " ")
   print()

#3.update values
from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T[2] = [11,9]
T[0][3] = 7
for r in T:
   for c in r:
      print(c,end = " ")
   print()

#4.delete values
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

del T[3]

for r in T:
   for c in r:
      print(c,end = " ")
   print()






"""
ISSUES FACED AND RESOLVED:
circular import error
"""