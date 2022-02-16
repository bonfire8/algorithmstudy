lst = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

N = len(lst)
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)