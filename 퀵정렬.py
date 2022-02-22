def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_arr, equal_arr, big_arr = [], [], []
    for i in arr:
        if i < pivot:
            less_arr.append(i)
        elif i > pivot:
            big_arr.append(i)
        else:
            equal_arr.append(i)
    return quicksort(less_arr) + equal_arr + quicksort(big_arr)

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
print(quicksort(arr))
