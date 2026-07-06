class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#1
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):

        #         if  prices[j]-prices[i] >= 0:
        #             new_profit = prices[j]-prices[i]
        #             profit = max(new_profit,profit)

        # return profit
        
#2
        # l = 0
        # r = 1

        # max_pro = 0

        # while r < len(prices):

        #     if prices[l] < prices[r]:
        #         pro = prices[r] - prices[l]
        #         max_pro = max(max_pro , pro)

        #     else :
        #         l = r

        #     r += 1

        # return max_pro


        # l - min price finade kare

#3
        buy = prices[0]
        profit = 0

        for p in prices:
            buy = min(buy , p)
            profit = max(profit , p-buy)
        return profit