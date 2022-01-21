"""
5
8 3 7 9 2
3
5 7 9
"""
N = int(input())
store = list(map(int, input().split()))
M = int(input())
consumer = list(map(int, input().split()))


def list_check(c):
    if c in store:
        print('yes', end=" ")
    else:
        print('no', end=" ")


def binary_check(s, e, target):
    if s > e:
        print('no', end=" ")
        return
    mid = (s + e) // 2
    if store[mid] == target:
        print('yes', end=" ")
    elif store[mid] > target:
        return binary_check(s, mid - 1, target)
    else:
        return binary_check(mid + 1, e, target)


for c in consumer:
    list_check(c)
print()
for c in consumer:
    binary_check(0, len(store) - 1, c)
