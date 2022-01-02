R, C = map(int, input().split())
x, y, d = map(int, input().split())

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]

MAP = []
for _ in range(R):
    MAP.append(list(map(int, input().split())))

check = 0  # 탈출 할 때
cnt = 1
MAP[x][y] = -1
while True:
    dx, dy = direction[d]  # 갈 곳
    d = (d + 1) % 4  # 방향 전환

    """갈 곳 바다인지 왔던 곳인지 체크"""
    a, b = x + dx, y + dy
    if MAP[a][b] == 1 or MAP[a][b] == -1:
        check += 1
        if check == 4:
            print(cnt)
            exit()
        continue
    """왔던 곳이나 바다가 아닐 시"""
    cnt += 1
    MAP[a][b] = -1  # 방문 지역 체크
    x, y = a, b  # 내 위치 변경
    check = 0
