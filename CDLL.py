class Node:
    def __init__(self, item=None,prev=None,next=None):
        self.item = item
        self.prev = prev
        self.next = next
        
        
class CDLL:
    def __init__(self, start=None):
        self.start = start
     
    # check the list is empty or not   
    def is_empty(self):
        return self.start == None
    
    # Insert at first in the list  
    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        self.start = n
        
    # Insert at last in the list
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            n.prev.next = n
            self.start.prev = n
    
    # Search element in the list
    def search(self, data):
        temp = self.start
        if temp == None:
            return None
        if temp.item == data:
            return temp
        else:
            temp = temp.next
            
        while(temp != self.start):
            if temp.item == data:
                return temp
            temp = temp.next   
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n
    
    # Print all elements of the list
    def print_list(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
            while(temp is not self.start):
                print(temp.item, end=' ')
                temp = temp.next
                
    # delete first element from the list
    def delete_first(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next
                
    
    # delete last element from the list
    def delete_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
    
    # delete element from the list
    def delete_element(self, data):
        if self.start is not None:
            temp = self.start
            if temp.item == data:
                self.delete_first()
            else:
                temp = temp.next
                while(temp is not self.start):
                    if temp.item == data:
                        temp.next.prev = temp.prev
                        temp.prev.next = temp.next
    
    
    # Make iterator function to make CDL class iterable
    def __iter__(self):
        return CDLLIterator(self.start)
    
class CDLLIterator:
    def __init__(self, start):
        self.start = start
        self.current = start
        self.first = True  # Track first iteration
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start is None:
            raise StopIteration
        
        # Stop when we return to start after first node
        if not self.first and self.current == self.start:
            raise StopIteration
        
        self.first = False
        data = self.current.item
        self.current = self.current.next
        return data
    
    
    

mylist = CDLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(30), 35)

for ele in mylist:
    print(ele,end=' ')
print()
print("***"*20)

mylist.print_list()
