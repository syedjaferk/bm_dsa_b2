# https://excalidraw.com/#json=wq2z-4RriNbSpODwSZXaW,mnCUPjxWC5O_e44k3aSM6A
# 

nums = [2,7,11,15]
target = 13

# brute force
def find_two_sum_index(nums, target): 
	total_nums = len(nums)
	for itr in range(total_nums):
		for jtr in range(itr+1, total_nums):
			if nums[itr] + nums[jtr] == target:
				 return [itr, jtr]

def find_two_sum_with_dict(nums, target):
	total_nums = len(nums)
	map_val = {}
	
	# 1st Iter
	for itr in range(total_nums):
		map_val[nums[itr]] = itr
	
	# 2nd Iter
	for itr in range(total_nums):
		res = target - nums[itr]
		if (res in map_val) and (itr != res):
			return itr, map_val[res]


def find_two_sum_with_dict_optimized(nums, target):
	total_nums = len(nums)
	map_val = {}
	
	for itr in range(total_nums):
		res = target - nums[itr]
		
		if res in map_val:
			return [itr, map_val[res]]
		
		map_val[nums[itr]] = itr

response = find_two_sum_with_dict_optimized(nums, target)
print(response)
