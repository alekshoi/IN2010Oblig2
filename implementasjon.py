
def BubbleSort(A): # O(n^2)
    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    return A

array = [2, 4, 3, 6, 5, 8, 3, 1]

print(BubbleSort(array))