class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        new=0
        for left in range(len(prices)):
            for right in range(left+1,len(prices)):
                new=prices[right] - prices[left]
                maxi = max(new,maxi)


        return maxi                

        