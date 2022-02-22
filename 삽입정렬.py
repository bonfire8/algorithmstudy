arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
# for i in range(1, len(arr)):
#     while arr[i] < arr[i-1]:
#         arr[i], arr[i-1] = arr[i-1], arr[i]
#         i -= 1

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
print(arr)