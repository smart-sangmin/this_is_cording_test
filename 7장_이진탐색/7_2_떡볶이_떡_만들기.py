"""
4 6
19 15 10 17
"""
N, M = map(int, input().split())
rice_cake_list = list(map(int, input().split()))

start = 0
end = max(rice_cake_list)


while start <= end:
    mid = (start + end) // 2
    total = 0
    for r in rice_cake_list:
        if r - mid > 0:
            total += (r - mid)
    if total >= M:
        start = mid + 1
    elif total < M:
        end = mid - 1

print(end)
