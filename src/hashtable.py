from queue import Queue

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def __len__(self):
        return len(self.storage)

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        if self.storage[idx] is None:
            self.storage[idx] = LinkedPair(key, value)
        elif self.storage[idx].key == key:
            self.storage[idx].value = value
        else:
            new_list_pair = LinkedPair(key, value)
            current = self.storage[idx]
            while current.next is not None:
                current = current.next
            current.next = new_list_pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        current = self.storage[idx]

        def find_value(hash_key, list_node):
            if list_node.key == hash_key:
                return list_node.value
            elif list_node.next is None:
                return None
            else:
                return find_value(hash_key, list_node.next)

        return find_value(key, current)

    def resize(self):

        queue = Queue()
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        prev_capacity = self.capacity
        self.capacity = self.capacity * 2
        new_hash_table = [None] * self.capacity
        for i in range(prev_capacity):
            if self.storage[i] is not None:
                queue.enqueue(self.storage[i])
                while len(queue) > 0:
                    node = queue.dequeue()
                    idx = self._hash_mod(node.key)
                    new_node = LinkedPair(node.key, node.value)

                    if new_hash_table[idx] is None:
                        new_hash_table[idx] = new_node
                    elif new_hash_table[idx].key == node.key:
                        new_hash_table[idx].value = node.value
                    else:
                        current = new_hash_table[idx]
                        while current.next is not None:
                            current = current.next
                        current.next = new_node

                    if node.next is not None:
                        queue.enqueue(node.next)

        self.storage = new_hash_table
        # for i in range(prev_capacity):
        #     current = self.storage[i]
        #     key = current.key
        #     value = current.value
        #     idx = self._hash_mod(key)
        #     if new_hash_table[idx] is None:
        #         new_hash_table = LinkedPair(key, value)
        #     else:
        #         new_node = LinkedPair(key, value)
        #         new_current = new_hash_table
        #         while new_current.next is not None:
        #             new_current = new_current.next
        #         new_current.next = new_node


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    print(f"Length of Storage: {len(ht)}")
    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
