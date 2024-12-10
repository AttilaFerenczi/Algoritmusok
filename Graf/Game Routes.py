MOD = 10**9 + 7

n, m = map(int, input().split())

edge = [[] for _ in range(n + 1)]
backedge = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)
dp = [0] * (n + 1)
dp[1] = 1

for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    backedge[b].append(a)
    in_degree[b] += 1

q = []
front = 0
back = 0

for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)
        back += 1

while front < back:
    node = q[front]
    front += 1

    for next_node in edge[node]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            q.append(next_node)
            back += 1

    for prev_node in backedge[node]:
        dp[node] = (dp[node] + dp[prev_node]) % MOD

print(dp[n])