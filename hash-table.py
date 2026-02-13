class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, string):
        result = 0
        for char in string:
            result += ord(char)
        return result

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            self.collection[hashed_key][key] = value
        else:
            self.collection[hashed_key] = {key : value}
    
    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            del self.collection[hashed_key][key]
    
    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            return self.collection[hashed_key][key]
        else:

            return None

