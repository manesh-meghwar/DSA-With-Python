class Stack(list):
    
    # Cheking whether stack is empty or not
    def is_empty(self):
        return len(self) == 0
    
    # Make push function
    def push(self, data):
        self.append(data)
        
    
    # Make pop function
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty2")
        
    # Make peek function
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
        
    # Make size function
    def size(self):
        return len(self)
    
    # Make function to restrict the insert function
    def insert(self, index, data):
        raise AttributeError("No attribute 'insert' in Stack")
    
    
s1 = Stack()
# s1.insert(0, 10)
s1.push(10)
s1.push(20)
s1.push(30)
print("Top value is :", s1.peek())