# making Queue Data Structure using Singly Linked List

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear  = None
        self.item_count = 0
        
    # make empty method
    def is_empty(self):
        return self.front == None
        # return self.rear == None              # Any of them you can use to check queue empty conditions
        # return self.item_count == 0
        
    # Insert Method
    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        
        self.rear  = n
        self.item_count += 1
    
    # Delete Method
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        elif self.front == self.rear:
            self.front = None
            self.rear  = None
        else:
            self.front = self.front.next
        self.item_count -= 1
        
    # Make get-frond value method
    def get_front(self):
        if self.is_empty():
            raise IndexError("No data found in the Queue....!")
        else:
            return self.front.item
    
    # Make get-rear value method
    def get_rear(self):
        if self.is_empty():
            raise IndexError("No data found in the queue...!") 
        else:
            return self.rear.item
    
    # Make a size method of the queue
    def size(self):
        return self.item_count


q1 = Queue()

q1.enqueue(10)           
q1.enqueue(20)           
q1.enqueue(30)           
q1.enqueue(40)      

print("Front => ", q1.get_front(), "Rear => ", q1.get_rear())     
print("Total Element in Queue : ", q1.size())
q1.dequeue()
print("------"*15, "After Deleted 1 Element ", "------"*15)
print("Front => ", q1.get_front(), "Rear => ", q1.get_rear())    
print("Total Element in Queue : ", q1.size()) 