'''
Jared Bawden
Project - Dictionaries
'''

class HashMap:
    ''' Uses LInear Probe to store key-value pairs '''
    INITIAL_CAPACITY = 8
    max_loadfactor = .8
    def __init__(self, initial_capacity=INITIAL_CAPACITY):
        ''' creates an empty HashMap'''
        self.lyst = [None] * initial_capacity
        self.num_keys = 0

    def get(self, key, default=None):
        ''' returns value of the key '''
        sum = 0
        for letter in key:
            sum += ord(letter)
        index = sum % self.capacity()
        while self.lyst[index] is not None:
            if self.lyst[index][0] == key:
                return self.lyst[index][1]
            index += 1
            if index == len(self.lyst):
                index -= len(self.lyst)
        return default

    def set(self, key, value):
        ''' adds the key-value pair to the hashmap. If load-factor is greater than 80%, rehash the map '''
        sum = 0
        for letter in key:
            sum += ord(letter)
        index = sum % self.capacity()
        while self.lyst[index] is not None:
            if self.lyst[index][0] == key:
                self.lyst[index][1] = value
                break
            index += 1
            if index == len(self.lyst):
                index -= len(self.lyst)
        if self.lyst[index] is None:
            self.lyst[index] = [key, value]
            self.num_keys += 1
        load_factor = self.num_keys/self.capacity()
        if load_factor > self.max_loadfactor:
            self.rehash()

    def clear(self):
        ''' emptys the hashmap '''
        self.lyst = [None] * 8
        self.num_keys = 0

    def capacity(self):
        ''' returns the current capacity, number of buckets '''
        return len(self.lyst)

    def size(self):
        ''' returns the number of key-value pairs in the map '''
        return self.num_keys

    def keys(self):
        ''' returns a list of keys '''
        lyst_of_keys = []
        for pair in self.lyst:
            if pair is not None:
                key = pair[0]
                lyst_of_keys.append(key)
        return lyst_of_keys

    def pairs(self):
        ''' returns a list of keys '''
        lyst_of_pairs = []
        for pair in self.lyst:
            if pair is not None:
                lyst_of_pairs.append(pair)
        return lyst_of_pairs

    def rehash(self):
        ''' rebuild the table that is twice the capacity of the current table '''
        all_pairs = self.pairs()
        self.lyst = [None]*(self.capacity()*2)
        self.num_keys = 0
        for pair in all_pairs:
            self.set(pair[0], pair[1])
