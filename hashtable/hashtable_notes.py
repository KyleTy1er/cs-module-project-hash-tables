
# hash table notes day 1:

'''

iterating through a list is O(n)...
this does not scale so well
hash tables can do it faster...

We need a magic box that tells us which index a certain
element is at...

if we could look up the index with a value that would
bring the time to O(1) - how do we make that happen?

point of interest:

certain data structures have certain performance
characteristics - cut to - THE HASH TABLE

all data structures have upsides and downsides
what are the downsides to hash tables?

the trade off is memory for speed - 

to create the magic box we need a

---------------------------------------------------------

"hashing function"

input: string
output: number
multiple inputs can give the same output("collisions")

* we have to take a string and turn it into a number *

ASCII is an encoding system for letters - for every letter
there is a corresponding number.

you can find the ASCII value of any letter with ord()
with ASCII every character is a byte

unicode is another way of encoding characters... it 
includes ASCII but goes beyond it - they are the same for
the first 127 characters but then unicode has much more.
beyond the 127 unicode are represented by multiple bytes
this is called UTF-8.

****-------------------------****
hashing functions tend to work on individual bytes so we
have to convert our string to a series of bytes.
you can think of a byte as a number between 0-255 inclusive.
****-------------------------****

.encode() is the way we will get our bytes...

'''

data = [0] * 16

# Size should be a power of 2
# that helps with stuff later
# you can end up with mismatched dist of keys

def my_hash(s):

    bites = s.encode()

    total = 0

    for b in bites:

        total += b

    return total



# using modulo "remainder" clamps it to a particular range
# the string is the key... and we store a value at that index

# this way of indexing can lead to collisions

# the remainder is O(1)
# but what is my_hash?

# we have to be clear about what the "n" in O(n) refers to...
# the get index is 0(1) over the look up, but not the key length?



def get_index(s):

	h = my_hash(s)

	i = h % len(data)

	return i

# print(my_hash("kyle"))
# print(my_hash("huh"))

# print(get_index("seven"))
# print(get_index("huh"))


def put(k, v):

	# get index into data to store value "v"
	i = get_index(k)
	# then store the value there
	data[i] = v


put("kyle", 1337)


def get(k):
	i = get_index(k)
	return data[i]

def delete(k):
	i = get_index(k)
	data[i] = 0


'''
Hash tables in particular languages:

Python: Dict
JavaScript: Object (Recently announced Map)
Swift: Dictionary, HashTable, HashMap

'''

