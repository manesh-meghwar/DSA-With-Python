# It is used to create c type ka array
import ctypes

class MeraList:
    def __init__(self):
        self.size = 1     # Initially we add only one element and then we resize it dynamically
        self.n = 0        # Initially the items are none/zero
        self.A = self.__make_array(self.size)  # Create a c type ka array with size -> self.size

    # we have make the cutom len() function as already python have
    def __len__(self):
        return self.n


    # Custom append function of MeraList class
    def append(self, item):
        # first check is array is full or empty
        if self.size == self.n:
            # Array is full so we have to -> resize
            self.__resize(self.size*2)

        # Otherwise we have to append it into the array & and increase the n or ++
        self.A[self.n] = item
        self.n = self.n + 1



    # Printing the L elements
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        # return result
        return '[' + result[:-1] + ']'


    # Pop Custom method
    def pop(self,item):
        if self.n == 0:
            return "Empty List"
        print(self.A[self.n-1])
        self.n = self.n-1

    # MAke a clear method of MeraList
    def clear(self):
        self.size = 1
        self.n =0

    # Find the elemnt in the List
    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "ValueError -> item not found"


    # Insert the element at position XX
    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n +1





    # Make __resize() method here
    def __resize(self, new_capacity):
        # Create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity

        # Copy the content of old array to new array
        for i in range(self.n):
            B[i] = self.A[i]
        # then reassign to A
        self.A = B
 

    def __make_array(self, capacity):
        # It is referential array (C type ka aray hai)
        return (capacity*ctypes.py_object)()  
    

L = MeraList()

L.append("Manesh")
L.append(29)
L.append("ML ENgineer")

# L.clear()
# L.pop(L)
L.insert(2,"AI-Engineer")
print(len(L))
print(L)

print(L.find(29))
# L.clear()




print("************"*15)


lst = []
lst.append("hello")
print(lst)
print(len(lst))