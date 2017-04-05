def reverse_order_of_words(lst):
	"""
	>>> reverse_order_of_words(['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'y', 'o', 'u'])
	['y', 'o', 'u', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

	"""

	res = []
	end = len(lst)

	for i in range(len(lst)-1, -1, -1):
		if lst[i-1] == ' ' or i == 0:
			for j in range(i, end):
				res.append(lst[j])
			if i != 0:
				res.append(' ')
			end = i -1
	return res

if __name__ == "__main__":
	import doctest
	results = doctest.testmod()
	if results.failed == 0:
		print "ALL TESTS PASSED"





