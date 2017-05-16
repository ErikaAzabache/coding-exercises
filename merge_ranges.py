def merge_ranges(lst):
	"""
	>>> merge_ranges([(0, 1), (3, 5), (6, 8), (9, 10), (11, 12)])
	[(0, 1), (3, 5), (6, 8), (9, 10), (11, 12)]
	>>> merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
	[(0, 1), (3, 8), (9, 12)]
	>>> merge_ranges([(0, 1), (3, 9), (4, 8), (10, 12), (9, 10)])
	[(0, 1), (3, 12)]
	"""
	# Strategy:
	# First order tuples by tup[0]
	# Compare tup[1] of lst[i] to tup[0] of lst[i+1]
	# if lst[i][1]<lst[i+1][0]
	# 	keep tuple as is, continue 
	# else: create a new tuple (lst[i][0], max(lst[i][1], lst[i+1][1])
	# compare this new tuple with lst[i+2] tuple to see if it can be further merged

	timeslots = []
	sorted_lst = sorted(lst, key=lambda tup: tup[0])
	i = 0

	while(sorted_lst):

		if (len(sorted_lst) == 1) or (sorted_lst[i][1] < sorted_lst[i+1][0]):
			timeslots.append(sorted_lst[i])
			sorted_lst.pop(0)
		else:
			new_tuple = (sorted_lst[i][0], max(sorted_lst[i][1], sorted_lst[i+1][1]))
			sorted_lst.pop(0)
			sorted_lst.pop(0)
			sorted_lst = [new_tuple] + sorted_lst

	return timeslots

if __name__ == "__main__":
	import doctest
	results = doctest.testmod()
	if results.failed == 0:
		print "ALL TESTS PASSED"
