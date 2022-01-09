"""
5 6
101010
111111
000001
111111
111111
"""

from collections import deque

N, M = map(int, input().split())
MAP = []
for i in range(N):
    MAP.append(list(map(int, input())))


def bfs():
    queue = deque()
    queue.append((0, 0))
    while queue:  # queue가 빌 때까지 반복
        x, y = queue.popleft()
        for a, b in ((1, 0), (0, 1), (-1, 0), (0, -1)):  # 네 방향 체크
            dx = x + a
            dy = y + b
            if dx < 0 or dx >= N or dy < 0 or dy >= M:  # 2차원 배열을 넘어갔을 때
                continue
            if MAP[dx][dy] == 1:
                MAP[dx][dy] += MAP[x][y]
                if dx == N - 1 and dy == M - 1:  # 도착지 도달 시 종료
                    return MAP[N - 1][M - 1]
                queue.append((dx, dy))


print(bfs())
