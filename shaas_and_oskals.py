n = int(input())
initial = list(map(int, input().split()))
x = int(input())
for _ in range(x):
    u, v = map(int, input().split())
    u -= 1  
    if u > 0:
        initial[u - 1] += v - 1 
    if u < n - 1:
        initial[u + 1] += initial[u] - v 
    initial[u] = 0 
for count in initial:
    print(count)