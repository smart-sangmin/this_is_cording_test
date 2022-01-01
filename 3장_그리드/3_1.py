N, M, K = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

total, cnt = 0, 0

for i in range(1, M + 1):
    if cnt == K:
        total += nums[-2]
        cnt = 0
        continue
    total += nums[-1]
    cnt += 1

print(total)
