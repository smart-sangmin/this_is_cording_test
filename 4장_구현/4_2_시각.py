N = int(input())
cnt = 0

for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if h % 10 == 3 or h // 10 % 10 == 3:
                cnt += 1
            elif m % 10 == 3 or m // 10 % 10 == 3:
                cnt += 1
            elif s % 10 == 3 or s // 10 % 10 == 3:
                cnt += 1
            """
            책 코드
            if '3' in str(h) + str(m) + str(s):
                cnt += 1
            """
print(cnt)