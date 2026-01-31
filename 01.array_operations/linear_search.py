def linear_search(arr, target):
	n = len(target)
	for index in range(n):
		if arr[index] == target:
			return index # return the index if we found target
	return -1 # if the target is not found 

arr = [2, 10, 11, 3, -1, 5, 7]
target = -1
response = linear_search(arr, target)
print(response)
