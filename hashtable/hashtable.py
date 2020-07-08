
# node
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.head = None

    def find_val(self, value):
        # start at the head
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur.value
            cur = cur.next
        return None

    def find_key(self, key):
        cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur.key
            cur = cur.next
        return None


    def insert_at_head(self, node):
        n = node
        # new value .next is current head
        n.next = self.head
        # current head is now set to n
        self.head = n

    def delete(self, value):
        cur = self.head
        # Special Case of Deleting Head:
        if cur.value == value: # are we deleting the head?
            self.head = self.head.next
            return cur
        # General Case
        prev = cur
        cur = cur.next
        while cur is not None:
            if cur.value == value:
                prev.next = cur.next # cuts out the node
                return cur
        else:
            prev = prev.next
            cur = cur.next
            return None


class HashTable:
    MIN_CAPACITY = 10

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.elements = 0

    def get_num_slots(self):

        return len(self.capacity)

    def djb2(self, key):
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        return self.djb2(key) % len(self.storage)

    def put(self, key, value):
        i = self.hash_index(key)
        if not self.storage[i]:
            hte = HashTableEntry(key, value)
            self.storage[i] = hte
            self.elements += 1
            hte.head = HashTableEntry(key, value)
        # need to account for if the key value is the same
        # how do I access the key value at this point?
        if self.storage[i].key == key:
            self.storage[i] = HashTableEntry(key, value)
        elif self.storage[i]:
            self.storage[i].insert_at_head(HashTableEntry(key, value))

    def get(self, key):
        # - find the index in the hash table for the key
        i = self.hash_index(key)
        # - search the list for that key
        if not self.storage[i]:
            return None
        else:
            if self.storage[i].find_key(key) == key:
                return self.storage[i].value

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.elements / self.capacity

    def resize(self, new_cap):
        prev_storage = self.storage
        self.capacity = new_cap
        self.storage = [None] * new_cap
        for i in range(len(prev_storage)):
            prev = prev_storage[i]
            if prev:
                while prev:
                    if prev.key:
                        self.put(prev.key, prev.value)
                        prev = prev.next

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        i = self.hash_index(key)
        node = self.storage[i]
        prev = None
        if node.key == key:
            self.storage[i] = node.next
            return
        while node != None:
            if node.key == key:
                prev.next = node.next
                self.storage[i].next = None
                return
            prev = node
            node = node.next
        self.elements -= 1
        return