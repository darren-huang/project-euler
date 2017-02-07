import time

def memoize(func):
	memo = {}
	def memoized_func(*args):
		nonlocal memo
		if args not in memo:
			memo[args] = func(*args)
		return memo[args]
	return memoized_func

def factorize(x):
	if x == 0:
		return 1
	return x*factorize(x-1)
factorize = memoize(factorize)

def ways_to_sum(sides, num_dice, sum):
	'''gives ways the "top dice" of the rolled dice can add up to 
	the desired sum ways_to_sum(6,3,15) gives all the ways you can 
	get a sum of 15 with 3 rolled dice with each 6 sides (numbered 1-6)'''
	if sum > num_dice * sides:
		return []
	elif sum <= 0:
		return []
	elif num_dice == 1:
		return [[sum]]

	return [[sides] + c for c in ways_to_sum(sides, num_dice - 1, sum - sides)] + \
		   ways_to_sum(sides - 1, num_dice, sum)

def permutations(num_elem, *item_occurences):
	'''gives you all the UNIQUE permutations of num_elem items where
	item_occurences state the occurneces of each unique item. Ex. ways
	to permutate AAABBB would be written by arrangements(6,3,3)'''
	denom = 1
	for num in item_occurences:
		denom = factorize(num)*denom
	return factorize(num_elem)/denom
permutations = memoize(permutations)


def time(str):
	start_time = time.time()
	eval(str)
	print("--- %s seconds ---" % (time.time() - start_time))
