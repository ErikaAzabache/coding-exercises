def max_product_of_3_int(lst):
	"""Given a list of integers, function finds the highest 
	product you can get from three of the integers in the list.
	>>> max_product_of_3_int([2, 4, 6, 3, 1])
	72
	>>> max_product_of_3_int([5, 10, 2, 4, 1])
	200
	>>> max_product_of_3_int([5, -5, 2, 4, 1])
	40
	>>> max_product_of_3_int([-10, -10, 1, 3, 2])
	300
	>>> max_product_of_3_int([-10, 10, 2, -5, -4])
	500
	>>> max_product_of_3_int([1, 10, -5, 1, -100])
	5000
	"""
	# BRUTE FORCE SOLUTION
	# max_prod = 1

	# for i in range(0, len(lst)):
	# 	for j in range(0, len(lst)):
	# 		for k in range(0, len(lst)):
	# 			if i == j or i == k or j == k:
	# 				continue
	# 			prod = lst[i] * lst[j] * lst[k]
	# 			max_prod = max(max_prod, prod)

	# return max_prod
	# A MORE OPTIMIZED SOLUTION
	# We need to traverse the list at least once to check the product of three

	# if we indeed only traverse once, we need to keep track of the highest_prod_3 and any combination 
	# of maximum product of two that multiplied by the current iteration, would give a new highest_prod_3.
	# This could be achieved by multiplying a current negative with the greatest negative number obtained
	# in the product of two numbers (lowest_prod_2) or a current number multiplied by the greatest positive product of two numbers (highest_prod_2). 
	# The highest_prod_2 and lowest_prod_2 should be updated if a greater negative (lowest) and positive (highest) is found.

	# Summing up, in each iteration we should kee track of:
	#		highest product of 3 numbers
	#		highest product of 2 numbers
	#		lowest product of 2 numbers
	#		highest number
	#		lowest number
	
	highest = max(lst[0], lst[1])
	lowest = min(lst[0], lst[1])

	highest_prod_2 = lst[0] * lst[1]
	lowest_prod_2 = lst[0] * lst[1]

	highest_prod_3 = lst[0] * lst[1] * lst[2]

	for i, current in enumerate(lst):
		if i == 0 or i == 1:
			continue
		highest_prod_3 = max(highest_prod_3, current*highest_prod_2, current*lowest_prod_2)

		highest_prod_2 = max(highest_prod_2, current*highest, current*lowest)
		lowest_prod_2 = min(lowest_prod_2, current*highest, current*lowest)
		
		highest = max(highest, current)
		lowest = min(lowest, current)

	return highest_prod_3



if __name__ == "__main__":
	import doctest
	results = doctest.testmod()
	if results.failed == 0:
		print "ALL TESTS PASSED!"

