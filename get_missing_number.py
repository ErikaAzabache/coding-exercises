def get_missing_number(lst):
	"""
	>>> get_missing_number([4, 5, 2, 1, 10])
	0
	>>> get_missing_number([4, 5, 2, 1, 0, 3, 6, 100])
	7
	"""
	hash_lst = (max(lst) + 1) * [0]

	for num in lst:
		hash_lst[num] = 1

	for i in range(len(hash_lst)):
		if hash_lst[i] == 0:
			return i

if __name__ == "__main__":
	import doctest
	results = doctest.testmod()
	if results.failed == 0:
		print "ALL TESTS PASSED"
