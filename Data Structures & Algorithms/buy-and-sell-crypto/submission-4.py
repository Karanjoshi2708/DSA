class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):

        #         if  prices[j]-prices[i] >= 0:
        #             new_profit = prices[j]-prices[i]
        #             profit = max(new_profit,profit)

        # return profit
        

        l = 0
        r = 1

        max_pro = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                pro = prices[r] - prices[l]
                max_pro = max(max_pro , pro)

            else :
                l = r

            r += 1

        return max_pro
