class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
    def __init__(self):
        self.head = None
    def add_to_head(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.bucket = [None] * capacity
        self.size = 0
        # Your code here


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return len(self.bucket)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        print(self.size/self.capacity)
        return self.size/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here
        FNV_prime = 1099511628211
        hash = 14695981039346656037
        for e in key:
            hash = hash * FNV_prime
            hash = hash^ord(e)
        return hash


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
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity*2)
        index = self.hash_index(key)
        hash_index = self.bucket[index]
        new_item = HashTableEntry(key, value)
        while hash_index != None and hash_index != key:
            hash_index = hash_index.next
        if hash_index != None:
            hash_index.value.add_to_head(new_item)
        else:
            new_list = LinkedList()
            new_list.add_to_head(new_item)
            new_entry = HashTableEntry(key, new_list)
            new_entry.next = self.bucket[index]
            self.bucket[index] = new_item
            self.size+=1
            print(new_item.value)


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        if self.get_load_factor()<0.2:
            self.resize(self.capacity*0.5)
        index = self.hash_index(key)
        hash = self.bucket[index]
        while hash != None:
            if hash.key == key:
                hash.value = None
                self.size -= 1
                return
            else:
                hash = hash.next
        print("Key not in HashTable")
        return



    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        hash = self.bucket[index]
        while hash != None:
            if hash.key == key:
                return hash.value
            else:
                hash = hash.next


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        old_volume = self.bucket
        new_volume = [None]*new_capacity
        self.bucket = new_volume
        self.capacity = new_capacity
        for x in old_volume:
            if x != None:
                self.put(x.key, x.value)



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