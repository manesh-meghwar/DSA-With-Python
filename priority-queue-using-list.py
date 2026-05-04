# Priority Queue class
class PriorityQueue:
    def __init__(self):
        self.items = []
        
    # Make a empty method
    def is_empty(self):
        return len(self.items) == 0
    
    # make a push() method:
    def push(self,data,priority):
        index = 0
        while index<len(self.items) and self.items[index][1]<=priority:
            index += 1
        self.items.insert(index, (data,priority))
       
    # Make a delete method 
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty...!")
        return self.items.pop(0)[0]
        
    # Make a size method
    def size(self):
        return len(self.items)
    
    
p = PriorityQueue()
p.push("Manesh", 4)
p.push("Mujhaid", 1)
p.push("Essa", 3)
p.push("Rizwan", 2)
p.push("Faizan", 6)
p.push("Muller", 5)

while not p.is_empty():
    print(p.pop())
    

    