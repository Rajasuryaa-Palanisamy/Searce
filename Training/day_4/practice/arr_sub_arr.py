#Find whether an array is subset of another array

def isSubset(arr1, m, arr2, n):
	
	hashset = set()

	for i in range(0, m):
		hashset.add(arr1[i])

	for i in range(0, n):
		if arr2[i] in hashset:
			continue
		else:
			return False

	return True

if __name__ == '__main__':
	
	arr1 = [ 11, 1, 13, 21, 3, 7 ]
	arr2 = [ 11, 3, 7, 1 ]
	
	m = len(arr1)
	n = len(arr2)
	
	if (isSubset(arr1, m, arr2, n)):
		print("arr2[] is subset of arr1[] ")
	else:
		print("arr2[] is not a subset of arr1[] ")


