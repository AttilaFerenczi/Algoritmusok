MOD = 10**9 + 7

def count_ways_to_split(n):
    S = n * (n + 1) // 2
    
    if S % 2 != 0:
        return 0
    
    target = S // 2
    
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for num in range(1, n + 1):
        for i in range(target, num - 1, -1):
            dp[i] = (dp[i] + dp[i - num]) % MOD
    
    return dp[target] * pow(2, MOD - 2, MOD) % MOD

n = int(input())

print(count_ways_to_split(n))
