t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    total_ones = s.count('1')
    result = total_ones * (n - 2) + n
    print(result)
