class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = inf
        max_profit = 0
        for i in prices:
            minimum = min(minimum, i)
            max_profit = max(max_profit, i-minimum)
        return max_profit