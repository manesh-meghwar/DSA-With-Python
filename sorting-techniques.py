# ================= Bubble sort techniques ========================================

def bubble_sort(data_list):
    for item in range(1,len(data_list)):
        for i in range(len(data_list)-item):
            if data_list[i]>data_list[i+1]:
                data_list[i], data_list[i+1] = data_list[i+1], data_list[i]
                

# this is enhanced version of bubble sort technique
def modified_bubble_sort(data_list):
    
    for item in range(1,len(data_list)):
        flag = False
        for i in range(len(data_list)-item):
            if data_list[i]>data_list[i+1]:
                data_list[i], data_list[i+1] = data_list[i+1], data_list[i]
                flag = True
        if not flag: # this only run when flag is False or you can write (if flg==False)
            break
                

print("================ Bubble sort ======================")

l = [3,1,8,5,10,15,12,20,9]
print(l)
print("====="*10)
bubble_sort(l)
print(l)
print()

print("======="*10)

print()
l = [3,1,8,5,10,15,12,20,9]
print(l)
print("====="*10)
modified_bubble_sort(l)
print(l)

# ================= Selection sort techniques ========================================

def selction_sort(data_list):
    n = len(data_list)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if data_list[j] < data_list[min_index]:
                min_index = j
        # Swap on the basis of min_index
        data_list[i], data_list[min_index] = data_list[min_index], data_list[i]
        
        

print()
print("================ selction sort ======================")

l2 = [64,34,80,22,33,11,44,66,55]
print("Unsorted List => ", l2)
print("====="*10)
selction_sort(l2)
print("Sorted List => ", l2)




# ================= insertion sort techniques ========================================


def insertion_sort(data_list):
    n = len(data_list)
    for i in range(1, n):
        temp = data_list[i]
        j = i-1
        while j>=0 and temp < data_list[j]:
            data_list[j+1] = data_list[j]
            j-=1
        data_list[j+1]=temp




print()
print("================ Insertion sort ======================")

l3 = [99,54,32,22,10,12,44,16,25]
print("Unsorted List => ", l3)
print("====="*10)
insertion_sort(l3)
print("Sorted List => ", l3)






# ================= Quick sort techniques ========================================


def quick_sort(data_list):
    if len(data_list)<=1:
        return data_list
    else:
        pivot = data_list[0]
        lesser_list = [x for x in data_list[1:] if x<=pivot]
        greater_list = [x for x in data_list[1:] if x>pivot]
        
        return quick_sort(lesser_list) + [pivot] + quick_sort(greater_list)




print()
print("================ Quick sort ======================")

l4 = [98,14,42,52,30,62,44,16,15]
print("Unsorted List => ", l4)
print("====="*10)
print("Sorted List => ", quick_sort(l4))



# ================= Merge sort techniques ========================================


def merge_sort(data_list):
    n = len(data_list)
    if n>1:
        mid = n//2
        left_list = data_list[:mid]
        right_list = data_list[mid:]
        
        merge_sort(left_list)
        merge_sort(right_list)
        
        i=j=k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                data_list[k] = left_list[i]
                i+=1
            else:
                data_list[k] = right_list[j]
                j+=1
            k+=1
            
        while i<len(left_list):
            data_list[k] = left_list[i]
            i+=1
            k+=1
        while j < len(right_list):
            data_list[k] = right_list[j]
            j+=1
            k+=1




print()
print("================ Merge sort ======================")

l5 = [99,19,72,57,39,60,40,86,25]
print("Unsorted List => ", l5)
print("====="*10)
merge_sort(l5)
print("Sorted List => ", l5)
