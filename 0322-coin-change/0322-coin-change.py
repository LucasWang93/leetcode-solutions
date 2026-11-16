class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)

        # TODO:
        # 1. Initialize base case
        # 2. Fill dp from 1 to amount
        # 3. Return -1 if unreachable

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

        return -1