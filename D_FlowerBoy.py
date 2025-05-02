import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    can_satisfy_prefix = [0] * (m + 1)
    can_satisfy_prefix[0] = -1
    a_ptr = 0
    for j in range(m):
        found = False
        while a_ptr < n:
            if a[a_ptr] >= b[j]:
                can_satisfy_prefix[j + 1] = a_ptr
                a_ptr += 1
                found = True
                break
            a_ptr += 1
        if not found:
            for k in range(j + 1, m + 1):
                can_satisfy_prefix[k] = n 
            break
    if can_satisfy_prefix[m] < n:
        print(0)
        return
    can_satisfy_suffix = [0] * (m + 1)
    can_satisfy_suffix[m] = n
    a_ptr = n - 1
    for j in range(m - 1, -1, -1):
        found = False
        while a_ptr >= 0:
            if a[a_ptr] >= b[j]:
                can_satisfy_suffix[j] = a_ptr
                a_ptr -= 1
                found = True
                break
            a_ptr -= 1
        if not found:
            for k in range(j, -1, -1):
                can_satisfy_suffix[k] = -1 
            break
    min_k = float('inf')

    for j in range(m): 
        if can_satisfy_prefix[j] < can_satisfy_suffix[j + 1]:
            min_k = min(min_k, b[j])

    if min_k == float('inf'):
        print(-1)
    else:
        print(min_k)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()