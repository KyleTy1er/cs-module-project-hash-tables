import math
import random

# Modify the code in this directory to build a
# lookup table so that it can finish running in under a minute.

#The lookup table can be built in advance by iterating over all
# values in the domain of the function and recording the results.

lookup_table = {}

def slowfun(x, y):

    # create the lookup table to hold the stuffs...


    # is this wrong to do an inner function?
    def slowfun_too_slow(x, y):

        if (x, y) not in lookup_table:
            v = math.pow(x, y)
            v = math.factorial(v)
            v //= (x + y)
            v %= 982451653
            lookup_table[x, y] = v

        elif (x, y) in lookup_table:
                print("found one")
                return lookup_table[x, y]

        return lookup_table[x, y]

    return slowfun_too_slow(x, y)

    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

'''

Output looks like this:

0: 2,4: 410731503
1: 6,5: 486616558
2: 4,5: 12615158
3: 4,4: 237974173
4: 13,5: 381057234
5: 2,4: 410731503
6: 3,5: 651679062
7: 6,4: 238640537
8: 12,4: 842313213
9: 11,4: 511248842

'''

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
#
#
# for i in range(50):
#     x = random.randrange(2, 14)
#     y = random.randrange(3, 6)
#     print(f'{i}: {x},{y}: {slowfun_too_slow(x, y)}')


# lookuptable = {}
#
# lookuptable[1, 2] = 3
#
# def check(x,y):
#     if (x, y) in lookuptable:
#         return lookuptable[x, y]
#
# print (check(1, 2))