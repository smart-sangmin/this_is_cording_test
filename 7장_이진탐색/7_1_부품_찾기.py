N = int(input())
store = list(map(int, input().split()))
M = int(input())
consumer = list(map(int, input().split()))

for c in consumer:
    if c in store:
        print('yes', end=" ")
    else:
        print('no', end=" ")