def get_bit(num, i):
	"""
	>>> get_bit(0b0101011001, 3)
	1
	>>> get_bit(0b1101011001, 5)
	0
	"""
	if not num & (1 << i):
		return 0
	return 1

def insert_number(M, N, j, i):
	"""inserts M into N from j to i bits
	>>> insert_number(0b10011, 0b10000000000, 6, 2)
	'0b10001001100'
	"""
	mask1 = -1 << i             # 11111110000
	mask2 = (1 << (j + 1)) - 1  # 00011111111
	mask =  mask1 & mask2 

	N = (M << i) & mask | N 
	return bin(N)



if __name__ == "__main__":
	import doctest
	results = doctest.testmod()
	if results.failed == 0:
		print "ALL TESTS PASSED!"
