"""
3
15
27
12
"""
import sys
input = sys.stdin.readline
n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))
for num in sorted(num_list, reverse=True):
    print(num, end=" ")