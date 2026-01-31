def delete_element(arr, target):
	n = len(arr)
	for itr in range(n):
		if target == arr[itr]: # Check if the target value is equal to current index (itr).
			for jtr in range(itr, n-1):
				"""
				If we found the element to be deleted, then move the n+1 item to n till n-1 elements.
				"""
				arr[jtr] = arr[jtr+1]
			arr.pop()
			return arr
	print("Element Not Found")
	return arr # Returning the whole arr, since we can't delete an element which is not present.



arr = [2, 10, 11, 3, -1, 5, 7]
target = -1
response = delete_element(arr, target)
print(response)

