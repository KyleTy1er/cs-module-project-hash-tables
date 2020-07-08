

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
        #Special Case of Deleting Head:
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


# Hash table can't have fewer than this many slots
# MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

<<<<<<< Updated upstream
    def __init__(self, capacity):
        # Your code here
=======
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.elements = 0
>>>>>>> Stashed changes


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
<<<<<<< Updated upstream
        # Your code here
=======
        return len(self.storage)
>>>>>>> Stashed changes


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.elements / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
<<<<<<< Updated upstream
        return self.djb2(key) % self.capacity
=======
        return self.djb2(key) % len(self.storage)
>>>>>>> Stashed changes

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
<<<<<<< Updated upstream
        # Your code here
=======
        # need to account for if the key value is the same   

        i = self.hash_index(key)
        if not self.storage[i]:
            hte = HashTableEntry(key, value)
            self.storage[i] = hte
            self.elements += 1
            hte.head = HashTableEntry(key, value)
        elif self.storage[i] and self.storage[i].key != key:
            self.storage[i].insert_at_head(HashTableEntry(key, value))
>>>>>>> Stashed changes


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
<<<<<<< Updated upstream
        # Your code here
=======
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
>>>>>>> Stashed changes


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
<<<<<<< Updated upstream
        # Your code here
=======
        # - find the index in the hash table for the key
        i = self.hash_index(key)
        # - search the list for that key
        if not self.storage[i]:
            return None
        else:
            if self.storage[i].find_key(key) == key:
                return self.storage[i].value
>>>>>>> Stashed changes


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
<<<<<<< Updated upstream
        # Your code here
=======
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

>>>>>>> Stashed changes



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
