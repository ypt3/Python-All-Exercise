class Stack:
    def __init__(self) -> None:
        # self.count = 0
        self.values = []

    def __len__(self):
        return len(self.values)
    
    def peek(self):
        return self.values[-1]
    
    def pop(self):
        return self.values.pop()    
    
    def push(self, value):
        self.values.append(value)

