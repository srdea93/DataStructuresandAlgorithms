class Hashtable():
    def __init__(self, size):
        self.size = size
        self.table = [None for i in range(self.size)]

    def hash(self, item):
        item_type = type(item)
        if item_type == str:
            item_ascii = [str(ord(letter)) for letter in item]
            item_ascii = int("".join(item_ascii))
            key = item_ascii % self.size
        elif item_type == int:
            key = item % self.size
        else:
            return KeyError
        return key

    def set(self, item_key, item_value):
        hash_key = self.hash(item_key)
        item = [item_key, item_value]
        while self.table[hash_key] is not None:
            hash_key = (hash_key + 1)%self.size
        self.table.insert(hash_key, item)
        return F"{item_key} inserted at {hash_key} with value {item_value}"

    def get(self, item_key):
        hash_key = self.hash(item_key)
        while item_key != self.table[hash_key][0]:
            if self.table[hash_key] is None:
                return None
            else:
                hash_key = (hash_key + 1)%self.size
        return self.table[hash_key]


# ------------------------ Test ------------------------
table = Hashtable(size=17)
item_keys = ['grapes', 'apples', 'grapples', 'oranges']
item_values = [100, 200, 300, 400]
for i in range(0,4):
    print(table.set(item_key=item_keys[i], item_value=item_values[i]))

print(table.get('grapples'))