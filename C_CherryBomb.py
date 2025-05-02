import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    found_x = False
    potential_x = -1

    for i in range(n):
        if b[i] != -1:
            if not found_x:
                potential_x = a[i] + b[i]
                found_x = True
            elif potential_x != a[i] + b[i]:
                print(0)
                return

    if found_x:
        for i in range(n):
            if b[i] == -1:
                required_bi = potential_x - a[i]
                if required_bi < 0 or required_bi > k:
                    print(0)
                    return
        print(1)
    else:
        max_val_a = a[0]
        for i in range(1, n):
            max_val_a = max(max_val_a, a[i])

        # calculate the upper bound for x: min(a[i] + k)
        min_val_a_plus_k = a[0] + k
        for i in range(1, n):
             min_val_a_plus_k = min(min_val_a_plus_k, a[i] + k)

        lower_bound_x = max_val_a
        upper_bound_x = min_val_a_plus_k

        count = max(0, upper_bound_x - lower_bound_x + 1)
        print(count)


t = int(sys.stdin.readline())
for _ in range(t):
    solve()