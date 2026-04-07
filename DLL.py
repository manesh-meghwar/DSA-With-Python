# Doubly Linked List

# Here create the node class
class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next
     
     
# Create the doubly link list class here   
class DLL:
    def __init__(self, start=None):
        self.start = start
    
    # this checks that is list empty or not
    def is_empty(self):
        return self.start == None
    
    # here to insert the item at first
    def inser_at_start(self, data):
        n = Node(Node, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n
    
    # here to insert the item at last
    def insert_at_last(self, data):
        temp = self.start
        if self.start != None:
            while temp.next != None:
                temp = temp.next
        n = Node(temp, data, None)
        if temp == None:
            self.start = n
        else:
            temp.next = n
    
    # here to search the item where it exists
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    
    # here to insert the item after a particular item
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n
            
    # here to print the all items of the list
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
            
    
    # here to delete the item at first
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
                
    
    # here to delete the item at last
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is None:
                temp = temp.next
            temp.next.prev = None
            
    
    # here to delete the item after a particular item
    def delete_item(self, data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                        
                temp = temp.next
    
    # here to create iterative for makin class Iterable
    def __iter__(self):
        return DLLIterator(self.start)
    
    
class DLLIterator:
    def __init__(self, start):
        self.current = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        
        return data
        
        
        
myList = DLL()
myList.inser_at_start(10)
myList.insert_at_last(20)
myList.insert_after(myList.search(10), 15)

for item in myList:
    print(item, end=" ")
    
print()