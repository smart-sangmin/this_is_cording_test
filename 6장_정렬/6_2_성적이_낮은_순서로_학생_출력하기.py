"""
2
홍길동 95
이순신 77
"""
import sys
input = sys.stdin.readline
N = int(input())
students = []
for _ in range(N):
    name, score = input().split()
    students.append((name, int(score)))
for student in sorted(students, key=lambda x: x[1]):
    print(student[0], end=" ")