from random import shuffle,randint

def create_array(size,max):
    return [randint(0,max) for _ in range(size)]

def is_sorted(arr):
    for i in range(1,len(arr)):
        if  arr[i]<arr[i-1]:
            return False
    return True

def bogo_sort(arr):
    iters=0
    while not is_sorted(arr):
        shuffle(arr)
        iters += 1
    return iters, arr
    
# arr = [1, 3, 2, 99, 4, 1]
arr = create_array(5,8)
print(f"unsorted array is {arr}")
iters, arr_s=bogo_sort(arr)
print(f"Number of iterations to sort are {iters}")
print(f"sorted array is {arr_s}")