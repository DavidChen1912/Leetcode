# bubble sort

def bubble_sort(arr):
    n = len(arr) 
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True
    return arr

arr = [64, 34, 25, 12, 22, 1]
a = bubble_sort(arr)
print(a)