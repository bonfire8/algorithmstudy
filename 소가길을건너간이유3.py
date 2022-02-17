#14469
T = int(input())
lst =[list(map(int, input().split())) for _ in range(T)]

s_lst = sorted(lst)

time = s_lst[0][0]
for l in s_lst:
    if l[0] <= time:
        time += l[1]
    else:
        time = l[0] + l[1]

print(time)

###
def time(T, lst):
    time = lst[0][0]
    for l in lst:
        if l[0] <= time:
            time += l[1]
        else:
            time = l[0] + l[1]

    return time

T = int(input())
lst =sorted(list(map(int, input().split())) for _ in range(T))

print(time(T, lst))