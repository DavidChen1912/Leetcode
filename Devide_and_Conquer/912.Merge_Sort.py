# merge sort

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    Left = merge_sort(arr[:mid])
    Right = merge_sort(arr[mid:])
    return merge (Left, Right)
def merge(Left, Right):
    merged = []
    i = j = 0
    while i < len(Left) and j < len(Right):
        if Left[i] < Right[j]:
            merged.append(Left[i])
            i +=1
        else:
            merged.append(Right[j])
            j +=1
            merged.extend(Left[i:])
            merged.extend(Right[j:])
            return merged
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))
