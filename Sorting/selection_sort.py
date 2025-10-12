# selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min_index = i 
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
     
arr = [64, 34, 25, 12, 22, 1]
a = selection_sort(arr)
print(a)