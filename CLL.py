# Make Node for Circular Linked List
class Node:
    # constructor initialization
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        
# Make Circular linked List class

class CLL:
    # constructor initialization
    def __init__(self, last=None):
        self.last = last
        
    # to check list is empty or not
    def is_empty(self):
        return self.last == None
    
    # Insert the item at the start of the list
    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            
    # Insert the item at the last of the list
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n
            
            
    # search item from the list
    def search(self,data):
        if self.is_empty():
            return None
        temp = self.last.next
        while(temp != self.last):
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        
        return None
    
    # Insert the data after a particular item in the list
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n
                
    # Print all elements of the list
    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=" ")
                temp = temp.next
            
            print(temp.item)
                
    
    # Delete item at start
    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next 
    # Delete item at last
    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next 
                temp.next = self.last.next
                self.last = temp
                    
    # Delete particular item from the list 
    def delete_item(self, data):
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item == data:
                    self.delete_first()
                else:
                    temp = self.last.next
                    
                    while(temp != self.last):
                        if temp.next == self.last:
                            if self.last.item == data:
                                self.delete_last()
                            break
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next 
                    
    # make a fuctions which makes class iterable
    def __iter__(self):
        if self.last == None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)
        
        

# make a iterator class for iterations
class CLLIterator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        
        data = self.current.item
        self.current = self.current.next
        return data
    
    

myCLL = CLL()
myCLL.insert_at_start(10)
myCLL.insert_at_start(20)
myCLL.insert_at_last(30)
myCLL.insert_at_last(40)
myCLL.insert_after(myCLL.search(10), 50)

for item in myCLL:
    print(item, end=" ")
print()
print("**"*50)

myCLL.print_list()
