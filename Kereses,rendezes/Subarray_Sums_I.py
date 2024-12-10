N, x = map(int, input().split())
a = list(map(int, input().split()))

l = 0
sum = 0
cnt = 0

for r in range(N):
    sum += a[r]
    
    while sum > x:
        sum -= a[l]
        l += 1
    
    if sum == x:
        cnt += 1

print(cnt)