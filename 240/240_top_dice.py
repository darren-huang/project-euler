import time

def memoize(func):
    '''makes a cache for functions'''
    memo = {}
    def memoized_func(*args):
        nonlocal memo
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return memoized_func

def factorial(x):
    if x == 0:
        return 1
    return x*factorial(x-1)
factorial = memoize(factorial)

def list_occurences(li):
    '''takes in a list of numbers (ORDERED) and returns the number of
    occurences of each item

    >>>list_occurences([1,2,3])
    [1,1,1]
    >>>list_occurences([1,1,1,2,2,3])
    [3,2,1]
    '''
    i, count, answer=0, 0, []
    while i < len(li):
        current = li[i]
        while i < len(li) and current == li[i]:
            count += 1
            i += 1
        answer.append(count)
        count = 0
    return answer

def ways_to_sum(sides, dices, sum_total):
    '''gives ways the "top dice" of the rolled dice can add up to 
    the desired sum ways_to_sum(6,3,15) gives all the ways you can 
    get a sum of 15 with 3 rolled dice with each 6 sides (numbered 1-6)'''
    if sum_total > dices * sides:
        return []
    elif sum_total <= 0:
        return []
    elif dices == 1:
        return [[sum_total]]

    return [[sides] + c for c in ways_to_sum(sides, dices - 1, sum_total - sides)] + \
           ways_to_sum(sides - 1, dices, sum_total)
ways_to_sum = memoize(ways_to_sum)

def perm_memoize(func):
    '''makes a cache for the permutations function: this is needed because
    permutations, arguments[1:] are commutative so this cache funciton
    sorts the arguments[1:]'''
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
        denom = factorial(num)*denom
    return factorial(num_elem)/denom
permutations = perm_memoize(permutations)

def arb_dice_perm(dices, highest_num):
    '''gives the number of permutations for the arbitrary dice (non-top dice)
    these dice have to be equal or less than the lowest top roll (given
    by the highest_num)

    >>>arb_dice_perm(2, 2) #[2,2], [2,1], [1,2], [1,1]
    4
    '''
    if dices == 0 and highest_num == 0:
        return 1
    return highest_num**dices
arb_dice_perm = memoize(arb_dice_perm)

def n_choose_r_unordered(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))
n_choose_r_unordered = memoize(n_choose_r_unordered)


def top_dice_perm(top_rolls, dices = 20): #TOP_ROLLS MUST BE ORDERED
    '''gives you the NUMBER of unique permutations of 'dices' number of 
    dices where the top rolls (greatest numbers) are contained in the list
    'top_rolls' provided that there are 'n' dices rolled (dices that aren't
    shown in the 'top_rolls' list are either equal to or less than the 
    lowest top roll)'''
    lowest_top_roll = top_rolls[-1]

    #assign values to variables, so the list of top_rolls doesn't need to be modified
    num_arb_rolls = dices - len(top_rolls) #the amount of arbitrary rolls (rolls not included in top_rolls)
    num_top_rolls = len(top_rolls)
    top_occurences = list_occurences(top_rolls)
    perm = 0
    while num_top_rolls <= dices:
        #ways to order the top_rolls TIMES ways to order the arbitary_rolls
        #TIMES the ways to interleave the top_rolls with the arb_rolls
        perm += permutations(num_top_rolls, *top_occurences) * \
                arb_dice_perm(num_arb_rolls, lowest_top_roll - 1) *\
                n_choose_r_unordered(dices, num_top_rolls)
        num_arb_rolls -= 1
        num_top_rolls += 1
        top_occurences[-1] += 1
    return perm


def top_dice_sum_perm(sides, dices, top_x, sum_total):
    perm = 0
    for top_rolls in ways_to_sum(sides, top_x, sum_total):
        perm += int(top_dice_perm(top_rolls, dices)) #conversion to int prevents double rounding
    return perm

print(top_dice_sum_perm(12,20,10,70)) #gives the correct answer !

####################################################################
##################       7448717393364181966        ################
####################################################################





##########RunTime Testing##################################################
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



