class Solution:

    def __init__(self):
        self.memo = []
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = [-666]*(amount+1)
        return self.dp(coins, amount)

    def dp(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        if self.memo[amount] != -666:
            return self.memo[amount]

        res = float('inf')

        for coin in coins:
            subproblem = self.dp(coins, amount-coin)
            if subproblem == -1:
                continue
            res = min(res, subproblem+1)
        self.memo[amount] = res if res != float('inf') else -1
        return self.memo[amount]


