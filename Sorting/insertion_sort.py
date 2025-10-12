# insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

    return arr
arr = [64, 34, 25, 12, 22, 1]
a = insertion_sort(arr)
print(a)