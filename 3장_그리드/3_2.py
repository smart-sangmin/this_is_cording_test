N, M = map(int, input().split())
cards = []
for _ in range(N):
    cards.append(min(list(map(int, input().split()))))
print(max(cards))
