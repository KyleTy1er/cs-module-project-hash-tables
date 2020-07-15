# hash table notes day 2:


# From yesterday:

data = [0] * 16

def my_hash(s):
    bites = s.encode()
    total = 0
    for b in bites:
        total += b
    return total

def get_index(s):
	h = my_hash(s)
	i = h % len(data)
	return i

def put(k, v):
	i = get_index(k)
	data[i] = v

def get(k):
	i = get_index(k)
	return data[i]

def delete(k):
	i = get_index(k)
	data[i] = 0



'''

We could create an array of linked lists,
linked list chaining -

must account for duplicates when doing put so that
the linked list doesnt just add the value twice
so you must make sure the key doesnt exist

variables:
key
value
index location - made up of hash // len storage
	- hash only depends on the key
node.next
entire array or dict


pseudocode for put:
 - find the index in the hash table for the key
 - search the list at that index
 	if it exists:
 		overwrite the value
 	if it doesnt:
 		make a new record
 		insert it somewhere in the list

RECOMMEND USING HASHTABLEENTRY CLASS for LINKED LIST

pseudocode for get:
- find the index in the hash table for the key
- search the list for that key
	if it exists:
		return the value
	else:
		return None

psuedocode for delete:
- find index in hash table for key
- search list at that index for key
	if it exists:
		delete entry
		return deleted value
	else:
		return None


'''
# this is sort of our "NODE"
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None # make this a linked list node
        # how do you set up multiple entries?
        # hst.next = val
        # hst.next.next = val ???

# this loosely corresponds to our HashTableEntry
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

# this is just a class to keep up with metadata about the Nodes
# but we can add additional functionality
# gives us a place to specify a head node

class LinkedList:
	def __init__(self, value):
		self.head = None

	def find(self, value):
		# start at the head
		cur = self.head
		while cur is not None:
			if cur.value == value:
				return cur.value
			# this moves us forward
		 	cur = cur.next
		return None # we didn't find it



	def insert_at_head(self, node):
		pass

	def delete(self, value):
		pass

ll = LinkedList()
ll.insert(11)
ll.insert(22)

a  = Node(11)
b = Node(22)

a.next = b

# head node?
head = a


# how do I find something?
# start at head and look along the values
# if you find your search return it...



