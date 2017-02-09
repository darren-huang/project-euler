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

def list_occurences(li):
	'''takes in a list of numbers (ORDERED) and returns the number of
	occurences of each item

	>>>list_occurences([1,2,3])
	[1,1,1]
	>>>list_occurences([1,1,1,2,2,3])
	[3,2,1]'''
	i, count, answer=0, 0, []
	while i < len(li):
		current = li[i]
		while i < len(li) and current == li[i]:
			count += 1
			i += 1
		answer.append(count)
		count = 0
	return answer

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
ways_to_sum = memoize(ways_to_sum)

def perm_memoize(func):
	memo = {}
	def memoized_func(*args):
		nonlocal memo
		key = (args[0],) + tuple(sorted(args[1:]))
		if key not in memo:
			memo[key] = func(*args)
		return memo[key]
	return memoized_func

def permutations(num_elem, *item_occurences):
	'''gives you all the UNIQUE permutations of num_elem items where
	item_occurences state the occurneces of each unique item. Ex. ways
	to permutate AAABBB would be written by arrangements(6,3,3)'''
	denom = 1
	for num in item_occurences:
		denom = factorize(num)*denom
	return factorize(num_elem)/denom
permutations_old = permutations
permutations = perm_memoize(permutations)

def top_dice_perm(top_rolls, dices = 20):
	'''gives you the NUMBER of unique permutations of 'dices' number of 
	dices where the top rolls (greatest numbers) are contained in the list
	'top_rolls' provided that there are 'n' dices rolled (dices that aren't
	shown in the 'top_rolls' list are either equal to or less than the 
	lowest top roll)'''
	arb_rolls = dices - len(top_rolls) #the amount of arbitrary rolls 
                                       #(rolls not included in top_rolls)
	top_occurences = list_occurences(top_rolls)
    if top_rolls[len(top_rolls) - 1] == 1:

    while len(top_rolls) < dices:

    '''NOTE: plan is to first assume that top_rolls has all the rolls and
    even the lowest number will not be rolled in the arbitrary rolls
    then for that set of top_rolls find the configurations by taking 
    (TOP ROLL PERMs) x (ARB ROLL PERMs (x ^ y)) x (WAYS OF INTERLEAVING)
    then increment so that the top rolls include more nad more of the lowest
    num'''

def timer(str):
	start_time = time.time()
	eval(str)
	print("--- %s seconds ---" % (time.time() - start_time))

def timetest():
	sets = ways_to_sum(12,10, 70)
	start_time = time.time()
	for s in sets:
		permutations(10, *list_occurences(s))
	print("memo--- %s seconds ---" % (time.time() - start_time))
	start_time = time.time()
	for s in sets:
		permutations_old(10, *list_occurences(s))
	print("old no memo but no list to tuple--- %s seconds ---" % (time.time() - start_time))



