

array = [1, 6, 2, 0, 8, 9, 11]



class Insertionsort:

    def Insertionsort(A):
        for i in range(len(A)-1):
            j = i
            while j > 0 and A[j-1] > A[j]:
                A[j-1], A[j] = A[j],A[j-1]
                j = j-1
        return A

    

    print(Insertionsort(array))
    



