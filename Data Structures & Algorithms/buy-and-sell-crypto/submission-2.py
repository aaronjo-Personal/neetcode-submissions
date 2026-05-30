class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # maxPro = 0
        # for i in range(len(prices)-1):
        #     if max(prices[i+1:]) - prices[i] > maxPro:
        #         maxPro = max(prices[i+1:]) - prices[i]
    
        # return maxPro

        maxPro=0
        for i in range(len(prices) - 1):
            j=i+1
            while j !=len(prices):
                if prices[j] - prices[i] > maxPro:
                    maxPro = prices[j] - prices[i]
                j+=1
        return (maxPro)