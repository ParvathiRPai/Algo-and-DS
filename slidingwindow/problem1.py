# time complexity is o(n) and space complexity is O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = low
        # r = high
        
        l=0
        r=1
        res =0
        
        while r< len(prices):
            if prices[l]< prices[r]:
                res = max(res, prices[r]-prices[l])
            else:
                l=r
            r+=1
        return res
                
                
            