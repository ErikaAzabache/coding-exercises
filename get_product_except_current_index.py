def get_product_except_current_index(lst):
	"""Function that returns the product of all numbers in the list except the number whose
	index is the same as the index in the result

	>>> get_product_except_current_index([2, 3, 4, 5])
	[60, 40, 30, 24]
	>>> get_product_except_current_index([1, 2, 3, 4])
	[24, 12, 8, 6]
	>>> get_product_except_current_index([2, 4, 5, 7])
	[140, 70, 56, 40]
	"""

	prod_before = 1
	res = []

	for i in range(0, len(lst)):
		if i != 0:		
			prod_before = prod_before * lst[i-1]
		res.append(prod_before)

	prod_after = 1

	for i in range(len(lst)-1, -1, -1):
		if i != len(lst)-1:
			prod_after = prod_after * lst[i+1]
		res[i] = res[i] * prod_after

	return res

if __name__ == "__main__":
	import doctest
	results = doctest.testmod()
	if results.failed == 0:
		print "ALL TEST PASSED!"












































	