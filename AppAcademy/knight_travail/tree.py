class Node:
    def __init__(self, value) -> None:
        self._value = value
        self._parent = None
        self._children = []
    
    @property
    def value(self):
        return self._value
    
    @property
    def children(self):
        return self._children
    
    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, new_parent):
        if self._parent:
            self._parent.remove_child(self)
        if new_parent:
            new_parent.add_child(self)
        self._parent = new_parent
    
    def add_child(self, child):
        if child not in self._children:
            self._children.append(child)
            child.parent = self
        
    def remove_child(self, child):
        if child in self._children:
            self.children.remove(child)
            child.parent = None

    def depth_search(self, value):
        # Check if the current node's value matches the target value
        if self._value == value:
            return self # Return the current node if it's a match
        
        # Recursively search in depth for the target value in the children nodes
        for child in self._children:
            result = child.depth_search(value)
            if result:
                return result
        return None # If not found in the current node for its children

    def breadth_search(self, value):
        # Initialize a queue with the root node
        queue = [self]

        while queue:
            # Dequeue the first node from the queue
            current = queue.pop(0)
            
            # Check if the current node's value matches the target value
            if current.value == value: 
                return current
            
            # Enqueue the childrent of the current node for further exploration
            queue.extend(current.children)

        return None