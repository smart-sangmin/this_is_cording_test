s = input()
location = [ord(s[0]) - ord('a'), int(s[1]) - 1]
move = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
cnt = 0

for a, b in move:
    x, y = location[1] + a, location[0] + b
    if 0 <= x < 8 and 0 <= y < 8:
        cnt += 1

print(cnt)
