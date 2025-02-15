class HashTable:
    def __init__(self, size):
        self.size = size
        #Initialize with lists
        self.table = [[] for _ in range(self.size)] 

    def hash_function(self, key):
        #Generate a hash for the key
        return hash(key) % self.size 

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    #Update the value if the key already exists
                    pair[1] = value
                    return True

            #Add a new key-value        
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        bucket = self.table[key_hash]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i] 
                return True 

        return False
    
# Testing the addition to the hash table
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print("\n--- Initial Values ---")
print(f"apple: {H.get('apple')}")  # Output: 10
print(f"orange: {H.get('orange')}")  # Output: 20
print(f"banana: {H.get('banana')}")  # Output: 30

# Testing the deletion from the hash table
print("\n--- Deleting 'apple' ---")
deleted = H.delete("apple")
print(f"Deleted 'apple': {deleted}")  # Output: True

print("\n--- Values After Deletion ---")
print(f"apple: {H.get('apple')}")  # Output: None (because the pair is deleted)
print(f"orange: {H.get('orange')}")  # Output: 20
print(f"banana: {H.get('banana')}")  # Output: 30