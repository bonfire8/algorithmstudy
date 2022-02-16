lst = [10, 6, 4, 8, 3, 1, 2, 9, 5, 7]

N = len(lst)
for i in range(N-1):
    minV = 9999
    for j in range(i, N):
        if minV > lst[j]:
            minV = lst[j]
            idx = j
    lst[i], lst[idx] = lst[idx], lst[i]
print(lst)