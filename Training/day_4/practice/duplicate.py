#To find a duplicate element in a limited range list
def findDuplicate(nums):
 
    visited = [False] * (len(nums) + 1)
 
    # for each element in the list, mark it as visited and
    # return it if seen before
    for i in nums:
 
        # if the element is seen before
        if visited[i]:
            return i
 
        # mark element as visited
        visited[i] = True
 
    # no duplicate found
    return -1
 
if __name__ == '__main__':
 
    nums = [1, 2, 3, 4, 4]
 
    print('The duplicate element is', findDuplicate(nums))
 
 