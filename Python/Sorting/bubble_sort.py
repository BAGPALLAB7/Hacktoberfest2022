def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
 
# Recursive function to perform bubble sort on sublist `A[i…n]`
def bubbleSort(A, n):
 
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            swap(A, i, i + 1)
 
    if n - 1 > 1:
        bubbleSort(A, n - 1)
 
 
if __name__ == '__main__':
 
    A = [ 3, 5, 8, 4, 1, 9, -2 ]
 
    bubbleSort(A, len(A))
 
    # print the sorted list
    print(A)