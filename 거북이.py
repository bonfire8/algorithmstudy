#2669
lst = list(map(int, input().split()))

s_lst= sorted(lst)
result = s_lst[0] * s_lst[2]
print(result)