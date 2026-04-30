class Node:
    def __init__(self, item, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next
        

class Deque:
    def __init__(self):
        self.front = None
        self.rear  = None
        self.item_count = 0
        
    # Check is Deque is empty or not
    def is_empty(self):
        return self.item_count == 0
    
    # Insert from front
    def insert_front(self, data):
        n = Node(data, None, self.front)
        if self.is_empty():
            self.rear  = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1
        
    # Insert from rear
    def insert_rear(self, data):
        n = Node(data, self.rear)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1
        
        
    # Delete from front
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is EMpty...!")
        elif self.front == self.rear:
            self.front = None
            self.rear  = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1
        
    # Delete from rear
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is EMpty...!")
        elif self.rear == self.front:
            self.rear = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count -= 1
        
    # get Element from front
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty...!")
        else:
            return self.front.item
    
    # get Element from rear
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty...!")
        else:
            return self.rear.item
        
    # make a size function
    def size(self):
        return self.item_count
    
    
d1 = Deque()

d1.insert_front(100)
d1.insert_front(200)
d1.insert_front(300)
d1.insert_rear(400)
d1.insert_rear(500)
print("Front => ", d1.get_front(), "Rear => ", d1.get_rear())
print("Length is => ",d1.size())
d1.delete_front()
d1.delete_rear()
print("------------------------------ After Delete from rear and front -------------------------------------")

print("Front => ", d1.get_front(), "Rear => ", d1.get_rear())
print("Length is => ",d1.size())

