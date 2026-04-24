class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        

class Stack:
    def __init__(self):
        self.top = None
        self.item_count = 0
        
    # Check stack is empty or not
    def is_empty(self):
        # return self.top == None
        return self.item_count == 0  # More efficient than checking top

    
    # Make a push function (For insertion fron top)
    def push(self, data):
        n = Node(data, self.top)
        self.top = n
        self.item_count += 1
        
    # Make a pop function (For deletion fron top)
    def pop(self):
        if not self.is_empty():
            data = self.top.item
            self.top = self.top.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("Stack is Empty/Underflow")
    
    # Make a peek function (For top Value of the stack)
    def peek(self):
        if not self.is_empty():
            return self.top.item
        else:
            raise IndexError("Stack is Empty/Underflow")
        
        
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        current = self.top
        while current:
            print(current.item, end=" -> ")
            current = current.next
        print("None")
    
    # Make a count function of the stack
    def size(self):
        return self.item_count
    
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.display()
print("Total elements in stack ", s1.size())
print("Top elements in stack ", s1.peek())
print("Pop element is ", s1.pop())
print("Total elements in stack ", s1.size())
print("Top elements in stack ", s1.peek())
print()
    