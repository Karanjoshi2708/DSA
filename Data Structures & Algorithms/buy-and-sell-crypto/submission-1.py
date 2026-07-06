class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):

                if  prices[j]-prices[i] >= 0:
                    new_profit = prices[j]-prices[i]
                    profit = max(new_profit,profit)

        return profit
        