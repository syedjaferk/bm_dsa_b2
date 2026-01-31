def binary_search(arr, target):
     low = 0
     high = len(arr) - 1
     while low <= high:
         mid = (low + high) // 2
         if arr[mid] == target:
             return mid
         elif arr[mid] < target:
             low = mid + 1
         else:
             high = mid - 1
     return -1

arr = [0 , 1, 7, 10, 100, 105, 201]
response = binary_search(arr, 100)
print(response)
