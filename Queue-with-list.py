# Making Queue class for Queue implement
class Queue:
    def __init__(self):
        self.items = []
        #self.front = None   # front (Deletion where from item deleted )                # here front and rear using but other language like java/C++ these properties are required
        #self.rear  = None   # rear (Insertion where from  item inserted )
        
    # Making empty function that checks whether queue is empty or not
    def is_empty(self):
        return len(self.items) == 0
    
    # Insert element function here
    def enqueue(self,data):
        self.items.append(data)
        
    
    # Delete element function here from last
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue is empty/underflow...!")
        
    # Get front value (Means get the first value)
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty/underflow...!")
    
    # Get rear value (Means get the last value)
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is Empty/Underflow")
        
    # make a size function for the queue
    def size(self):
        return len(self.items)
    
    
q1 = Queue()

try:
    q1.get_front()
except IndexError as e:
    print(e.args[0])
    
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("Front => ", q1.get_front(), "Rear => ",  q1.get_rear())

try:
    q1.dequeue()
    print("Remaining data elements are :", q1.size())
except IndexError as e:
    print(e.args[0])