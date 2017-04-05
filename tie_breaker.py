def tie_breaker(scores):
	"""Function that takes scores as a list of tuples (name, points)
	and returns a roster as a list of tuples (name, place), where
	a person is placed in a position regardless of a tie in previous positions

	For example:
	>>> tie_breaker([('Adam', 30), ('Bob', 56), ('Erika', 80), ('David', 67), ('Zoey', 67)])
	[('Erika', 1), ('David', 2), ('Zoey', 2), ('Bob', 4), ('Adam', 5)]

	>>> tie_breaker([('Adam', 30), ('Bob', 67), ('Erika', 80), ('David', 80), ('Zoey', 67)])
	[('David', 1), ('Erika', 1), ('Bob', 3), ('Zoey', 3), ('Adam', 5)]

	>>> tie_breaker([('Adam', 30), ('Aaron', 30), ('Erika', 0), ('David', 0), ('Emma', 67)])
	[('Emma', 1), ('Aaron', 2), ('Adam', 2), ('David', 4), ('Erika', 4)]

	>>> tie_breaker([('Adam', 0), ('Aaron', 0), ('Erika', 0), ('David', 0), ('Emma', 0)])
	[('Aaron', 1), ('Adam', 1), ('David', 1), ('Emma', 1), ('Erika', 1)]
	"""
	scores = sorted(scores, key=lambda tup: (-tup[1], tup[0])) # making sure that if there's a tie, it orders alphabetically
	roster = [] # roster[i] = (name, position)
	previous_points = -1
	tie_breaking_position = 1

	for name, points in scores:
		if previous_points == points:
			roster.append((name, roster[-1][1]))
		else:
			roster.append((name, tie_breaking_position))

		previous_points = points
		tie_breaking_position += 1

	return roster

if __name__ == "__main__":
	import doctest
	results = doctest.testmod()
	if results.failed == 0:
		print "ALL TESTS PASSED!"
