"""
============================================================================
Implementation Exercise: Singly Linked List
============================================================================

-------
Phase 1:
-------
1. Node and LinkedList initialization
2. Getting a node by its position
3. Adding a node to the list's tail
4. Adding a node to list's head
5. Removing the head node
6. Removing the tail node
7. Returning the list length

-------
Phase 2:
-------

1. Check whether the list contains_value a value
2. Inserting a node value into the list at a specific position
3. Updating a list node's value at a specific position
4. Removing a node value from the list at a specific position
5. Format the list as a string whenever `print()` is invoked
"""



# TODO: Implement a Linked List Node class here

class Node: 
    def __init__(self, value) -> None:
        self._value = value 
        self._next = None 


class LinkedList: 
    def __init__(self) -> None:
        self._head = None 
        self._tail = None 
        self._length = 0

    def get_node(self, position):
        if position < 0 or position > self._length:
            raise IndexError("Invalid position")

        current = self._head 
        for _ in range(position):
            current = current._next
        
        return current
    
    def add_to_tail(self, value):
        new_node = Node(value)

        if self._head is None: 
            self._head = new_node
        else: 
            self._tail._next = new_node
        
        self._tail = new_node
        self._length += 1

    def add_to_head(self, value):
        new_node = Node(value)

        if self._head is None: 
            self._tail = new_node

        new_node._next = self._head
        self._head = new_node
        self._length += 1

    def remove_head(self):
        if self._head is None: 
            return None 
        
        removeed_value = self._head._value
        self._head = self._head._next
        self._length -= 1

        if self._head is None: 
            self._tail = None

        return removeed_value
    
    def remove_tail(self):
        current = self._head 

        if current is None: 
            return None
        
        if current._next is None: 
            value = current._value
            self._head = None 
            self._tail = None 
            self._length -= 1
            return value
        
        while current._next._next:
            current = current._next
        
        value = current._next._value
        current._next = None
        self._tail = current
        self._length -= 1
        return value
        
    def __len__(self):
        return self._length
        

# 1. Test Node and LinkedList initialization
node = Node('hello')
print(node)                                     # <__main__.Node object at ...>
print(node._value)                              # hello
linked_list = LinkedList()
print(linked_list)                              # <__main__.LinkedList object at ...>

# 2. Test getting a node by its position
# print(linked_list.get_node(0))                # None

# 3. Test adding a node to the list's tail
linked_list.add_to_tail('new tail node')
print(linked_list.get_node(0))                # <__main__.Node object at ...>
print(linked_list.get_node(0)._value)         # `new tail node`

# 4. Test adding a node to list's head
linked_list.add_to_head('new head node')
print(linked_list.get_node(0))                # <__main__.Node object at ...>
print(linked_list.get_node(0)._value)         # `new head node`

# 5. Test removing the head node
# linked_list.remove_head()
# print(linked_list.get_node(0)._value)         # `new tail node` because `new head node` has been removed
# print(linked_list.get_node(1))                # `None` because `new head node` has been removed

# 6. Test removing the tail node
# print(linked_list.get_node(0)._value)         # `new tail node`
# linked_list.remove_tail()
# print(linked_list.get_node(0))                # None

# 7. Test returning the list length
print(len(linked_list))                                 # 2