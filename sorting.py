def sort(lst):
	
	n = len(lst)
	for i in range(n):
		for j in range(n-i-1):
			if lst[j]>lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]
	return lst
	
n = int(input("Enter the size of the list: "))
nums = [] 
for i in range(n):
	nums.append(int(input()))	
	
print("List: ", nums)	
sorted_list = sort(nums)
print("Sorted List: ", sorted_list)


