def elevator_rides(n, max_weight, people):
    limit = 1 << n
    dp = [(float('inf'), float('inf'))] * limit
    dp[0] = (1, 0)

    for mask in range(1, limit):
        best_rides, best_weight = float('inf'), float('inf')
        for i in range(n):
            if mask & (1 << i):
                prev_mask = mask ^ (1 << i)
                prev_rides, prev_weight = dp[prev_mask]

                if prev_weight + people[i] <= max_weight:
                    current_rides, current_weight = prev_rides, prev_weight + people[i]
                else:
                    current_rides, current_weight = prev_rides + 1, people[i]

                if (current_rides < best_rides or
                        (current_rides == best_rides and current_weight < best_weight)):
                    best_rides, best_weight = current_rides, current_weight

        dp[mask] = (best_rides, best_weight)

    return dp[limit - 1][0]

n, max_weight = map(int, input().split())
people = list(map(int, input().split()))

print(elevator_rides(n, max_weight, people))