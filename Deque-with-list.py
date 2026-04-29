class Deque:
    def __init__(self):
        self.items = []
        
    # Empty function
    def is_empty(self):
        return len(self.items) == 0
    
    # insert from front
    def insert_front(self, data):
        self.items.insert(0,data)
        
    # insert from rear
    def insert_rear(self, data):
        self.items.append(data)
        
    # Delete fron front
    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Deque is Empty")
    
    # Delete from rear 
    def delete_rear(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("Deque is Empty...!")
    
    # Get element from front
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty....!")
        else:
            return self.items[0]
    
    # Get element from rear
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty....!")
        else:
            return self.items[-1]
    
    # make size method
    def size(self):
        return len(self.items)
    
    
d1 = Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
d1.insert_front(600)
d1.insert_rear(500)

print("Front Value => ",d1.get_front(), "Rear Value => ",d1.get_rear())
print("Total Elements => ", d1.size())
d1.delete_front()
d1.delete_rear()
print("---"*20,"After delete from front and rear ","---"*20)
print("Front Value => ",d1.get_front(), "Rear Value => ",d1.get_rear())
print("Total Elements => ", d1.size())


    