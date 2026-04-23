class Stack:
    def __init__(self):
        self.items = []
    
    # Checking whether list is empty or not
    def is_empty(self):
        return len(self.items) == 0
    
    # make push function 
    def push(self, data):
        self.items.append(data)
        
    
    # make pop function 
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")
        
    # Make peek functioin
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")
        
    # Make size function of the stack
    def size(self):
        return len(self.items)
    
    
    

s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top element is : ", s1.peek())
print("Removed element is : ", s1.pop())
print("Top element is : ", s1.peek())
print()