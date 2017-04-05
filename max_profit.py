def max_stock_profit(lst):
	"""Function that returns max profit that can be made by selling high after buying low.
	If rice doesn't change it returns 0. If price decreases, it returns the min loss

	>>> max_stock_profit([30, 50, 25, 35, 10, 15])
	20
	>>> max_stock_profit([30, 20, 15, 12, 10, 8])
	-2
	>>> max_stock_profit([10, 10, 10, 10, 10, 10])
	0
	"""
	if len(lst) < 2:
		raise IndexError("At least two stock values needed to buy and sell")

	min_price = lst[0]
	max_profit = lst[1] - lst[0]

	for index, current_price in enumerate(lst):
		if index == 0:
			continue

		currrent_profit = current_price - min_price
		max_profit = max(max_profit, currrent_profit)
		min_price = min(min_price, current_price)

	return max_profit

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"

