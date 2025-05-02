import sys

def solve():
    n, x = map(int, sys.stdin.readline().split())

    if n == 1:
        print(0)
        return

    if x == 0:
        for i in range(1, n):
            print(i, end=" ")
        print(0)
    elif x < n:
        for i in range(x):
            print(i, end=" ")
        for i in range(x + 1, n):
            print(i, end=" ")
        print(x)
    else: # x == n
       
        for i in range(n):
            print(i, end=" ")
        print()

t = int(sys.stdin.readline())
for _ in range(t):
    solve()