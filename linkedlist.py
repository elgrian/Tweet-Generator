#!python

class Node(object):

    def __init__(self, data):

        self.data = data
        self.next = None

    def __repr__(self):
    
        return 'Node({!r})'.format(self.data)


class LinkedList(object):
    

    def __init__(self, items=None):

        self.head = None  
        self.tail = None  
    
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):

        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        return 'LinkedList({!r})'.format(self.items())

    def items(self):

        items = [] 

        node = self.head  
        
        while node is not None: 
            items.append(node.data)  
            
            node = node.next  
        
        return items  

    def is_empty(self): 
        return self.head is None

    def length(self):

        counter = 0 
        for item in self.items():
            counter += 1
        return counter

    def append(self, item):

        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node 
        else: 
            self.tail.next = node 
            self.tail = node

    def prepend(self, item):

        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else: 
            node.next = self.head
            self.head = node

    def find(self, quality):

        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            else:
                node = node.next
        return None

    def find_node(self, quality):
        node = self.head
        while node is not None:
            if quality(node.data):
                return node
            else:
                node = node.next
        return None

    def delete(self, item):

        if self.is_empty():
            raise ValueError("Linked list is empty")

        if self.head.data == item:
            self.head = self.head.next 
            if self.tail.data == item:
                self.tail = None
            return

        current_node = self.head
        previous_node = None
        while current_node: 
            if current_node.data != item:
                previous_node = current_node
                current_node = current_node.next
            else:
                if self.tail.data == item:
                    if previous_node:
                        previous_node.next = None
                        self.tail = previous_node
                        return
                    else:
                        self.head = None
                        self.tail = None
                        return
                else:
                    previous_node.next = current_node.next
                    return
        raise ValueError('Item not found: {}'.format(item))

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))


    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

if __name__ == '__main__':
    test_linked_list()