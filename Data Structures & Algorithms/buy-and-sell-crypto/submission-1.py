class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        l, r = 0, 1

        while r < len(prices):
            cost = prices[l]
            rev = prices[r]
            if cost < rev:
                prof = rev - cost
                max_prof = max(max_prof, prof)
            else:
                l = r
            r += 1
        return max_prof
            
            
        