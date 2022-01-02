N = int(input())
location = [0, 0]
matrix = [[] * N for _ in range(N)]

c = ('L', 'R', 'U', 'D')
d = ((0, -1), (0, 1), (-1, 0), (1, 0))

command = input().split()

for cmd in command:
    x, y = location[0] + d[c.index(cmd)][0], location[1] + d[c.index(cmd)][1]
    if x < 0 or x >= N or y < 0 or y >= N:
        continue
    location = x, y

print(location[0] + 1, location[1] + 1)
