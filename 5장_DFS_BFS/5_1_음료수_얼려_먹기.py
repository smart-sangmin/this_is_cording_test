"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""
N, M = map(int, input().split())

ice = []
for _ in range(N):
    ice.append(list(map(int, input())))
cnt = 0


def DFS(a, b):
    if a < 0 or b < 0 or a >= N or b >= M or ice[a][b] != 0:
        return
    ice[a][b] = -1
    for x, y in ((a - 1, b), (a + 1, b), (a, b + 1), (a, b - 1)):
        DFS(x, y)


for i in range(N):
    for j in range(M):
        if ice[i][j] == 0:
            DFS(i, j)
            cnt += 1
print(cnt)
