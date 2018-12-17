#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):

        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):

        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):

        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):

        return hash(key) % len(self.buckets)

    def keys(self):

        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):

        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):

        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):

        entry_count = 0 

        for bucket in self.buckets:

            entry_count += bucket.length()
        return entry_count

    def contains(self, key): 

        index = self._bucket_index(key)
        bucket = self.buckets[index] 
        current_node = bucket.head
        while current_node is not None:
            if current_node.data[0] == key: 
                return True
            current_node = current_node.next 
        return False 

    def get(self, key): 

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        current_node = bucket.head
        while current_node is not None:
            return current_node.data[1]
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if bucket.find(lambda tuple: tuple[0] == key) is not None:
            node = bucket.find_node(lambda tuple: tuple[0] == key)
            node.data = (key, value) 
        else:
            bucket.append((key, value))


    def delete(self, key):

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if bucket.find(lambda tuple: tuple[0] == key) is not None:
            node = bucket.find_node(lambda tuple: tuple[0] == key)
            bucket.delete(node.data)
        else:
            raise KeyError("Key not found: {}".format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10), ('X', 11)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))


    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()