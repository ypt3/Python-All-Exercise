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
        pass

    def breadth_search(self, value):
        pass