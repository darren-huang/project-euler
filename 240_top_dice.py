def ways_to_sum(sides, num_dice, sum):
	if sum > num_dice * sides:
		return []
	elif sum <= 0:
		return []
	elif num_dice == 1:
		return [[sum]]

	return [[sides] + c for c in ways_to_sum(sides, num_dice - 1, sum - sides)] + \
		   ways_to_sum(sides - 1, num_dice, sum)
