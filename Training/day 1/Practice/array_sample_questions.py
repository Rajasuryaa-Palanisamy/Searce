#using numpy module
#1. array copy
# 1.1 shallow copy

from numpy import *                 
print("\n 1.1 shallow copy")  
# creating the first array
arr1 = array([2, 6, 9, 4])
 
# displaying the identity of arr1
print(id(arr1))
 
# shallow copy arr1 in arr2 using view()
arr2 = arr1.view() 
 
# displaying the identity of arr2
print(id(arr2))
  
# making a change in arr1
arr1[1] = 7                       
  
# displaying the arrays
print(arr1)
print(arr2)

#1.2 deep copy
print("\n 1.2 deep copy")
from numpy import *                 
  
# creating the first array
arr1 = array([2, 6, 9, 4])
 
# displaying the identity of arr1
print(id(arr1))
 
# shallow copy arr1 in arr2 using view()
arr2 = arr1.copy()
 
# displaying the identity of arr2
print(id(arr2))
  
# making a change in arr1
arr1[1] = 7                       
  
# displaying the arrays
print(arr1)
print(arr2)


#2.Write a Python program to find whether a given array of integers contains any duplicate element. Return true if any value appears at least twice in the said array and return false if every element is distinct.
print("\n test duplicates")
def test_duplicate(array_nums):
    nums_set = set(array_nums)    
    return len(array_nums) != len(nums_set)     
print(test_duplicate([1,2,3,4,5]))
print(test_duplicate([1,2,3,4, 4]))
print(test_duplicate([1,1,2,2,3,3,4,4,5]))

#3.Write a Python program to find the first duplicate element in a given array of integers. Return -1 If there are no such elements.
print("\n 3. printing first duplicate occurence")
def find_first_duplicate(nums):
    num_set = set()
    no_duplicate = "no duplicate"

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate

print(find_first_duplicate([1, 2, 3, 4, 4, 5]))
print(find_first_duplicate([1, 2, 3, 4]))
print(find_first_duplicate([1, 1, 2, 3, 3, 2, 2]))

#4.Write a Python program to find a pair with highest product from a given array of integers.
print("\n 4.max product pair")
def max_Product(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        print("No pairs exists") 
        return      
    # Initialize max product pair 
    x = arr[0]; y = arr[1] 

    # Traverse through every possible pair     
    for i in range(0, arr_len): 

        for j in range(i + 1, arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 

    return x,y    

nums = [1, 2, 3, 4, 7, 0, 8, 4] 
print("Original array:", nums)
print("Maximum product pair is:", max_Product(nums))

#5.Write a Python program to remove all duplicate elements from a given array and returns a new array.
import array as arr
print("\n 5.remove duplicates")
def test(nums):
    return sorted(set(nums),key=nums.index)

array_num = arr.array('i', [1, 3, 5, 1, 3, 7, 9])
print("Original array:")
for i in range(len(array_num)):    
    print(array_num[i], end=' ')
print("\nAfter removing duplicate elements from the said array:")
result = arr.array('i', test(array_num))
for i in range(len(result)):    
    print(result[i], end=' ')
