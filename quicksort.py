import math
array = [0,4,2,1,5,7,11,10]
array2 = [0,4,2,1,5,7,11,10,23,3, 4]


def Choosepivot(A, low, high):
    median = math.floor((low + high) / 2)

    return median



def Partition(A, low, high):
    p = Choosepivot(A, low, high)
    A[p], A[high] = A[high], A[p]


    pivot = A[high]
    left = low
    right = high - 1

    while left <= right:
        while left <= right and A[left] <= pivot:
            left = left + 1
            
        while right >= left and A[right] >= pivot:
            right = right - 1
            
        
        if left < right:
            A[left], A[right] = A[right], A[left]
      


    A[left], A[high] = A[high], A[left]
    return left



def Quicksort (A, low, high):
    if low >= high:
        return A
    
    p = Partition(A, low, high)
    Quicksort(A,low,p-1)
    Quicksort(A, p+1, high)
    return A


print(Quicksort(array2, 0, 10))