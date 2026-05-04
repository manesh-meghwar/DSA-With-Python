class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item = item
        self.priority = priority
        self.next = next


# Priority Queue class
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0
        
        
    # Make a empty method
    def is_empty(self):
        return self.start == None
    
    # make a push() method:
    def push(self,data,priority):
        n = Node(data,priority)
        if not self.start or priority<self.start.priority:
            n.next = self.start
            self.start = n
        else: 
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1
            
       
    # Make a delete/po method 
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty...!")
        data = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return data
        
    # Make a size method
    def size(self):
        return self.item_count
    
    
p = PriorityQueue()
p.push("Manesh", 4)
p.push("Mujhaid", 1)
p.push("Essa", 3)
p.push("Rizwan", 2)
p.push("Faizan", 6)
p.push("Muller", 5)

while not p.is_empty():
    print(p.pop())
    

    