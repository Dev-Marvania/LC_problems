class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        @cache
        def maxdiff(i):
            if i == n:
                return 0
            a = b = c = -5e7
            if i<n:
                a = stoneValue[i] - maxdiff(i+1)
            if i+1<n:
                b = stoneValue[i]+stoneValue[i+1] - maxdiff(i+2)
            if i+2<n:
                c = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - maxdiff(i+3)
            
            return max(a,b,c)

        val = maxdiff(0)    
        return "Alice" if val>0 else "Bob" if val<0 else "Tie"