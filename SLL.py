class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
        
        
class SLL:
    def __init__(self, start=None):
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        node = Node(data, self.start)
        self.start = node
        
    def insert_at_last(self, data):
        node = Node(data, None)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        else:
            self.start = node
    
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            else:
                temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            node = Node(data,temp.next)
            temp.next = node
    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()
        
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None 
            
    def delete_item(self, data):
        if self.start is None:
            return
        
        # If first node contains the data
        if self.start.item == data:
            self.start = self.start.next
            return
        
        # Search for the node to delete
        temp = self.start
        while temp.next is not None:
            if temp.next.item == data:
                temp.next = temp.next.next
                return
            temp = temp.next
            
        print(f"Item {data} not found in list")
                    
                
            
            
myList = SLL()
myList.insert_at_start(20)
myList.insert_at_start(10)
myList.insert_at_start(30)
myList.insert_at_last(50)
myList.insert_after(myList.search(10),25)
myList.print_list()
print()
myList.delete_item(20)
myList.print_list()
print()
myList.delete_last()
myList.print_list()
print()
myList.delete_first()
myList.print_list()


    
