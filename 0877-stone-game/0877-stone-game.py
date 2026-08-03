class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[None] * n for _ in range(n)]

        if n%2 == 0:
            return True

        def maxdiff(i,j):
            if i==j:
                return piles[i]

            if dp[i][j] is not None:
                return dp[i][j]

            dp[i][j] = max(piles[i]-maxdiff(i+1,j),piles[j]-maxdiff(i,j-1)) 
            return dp[i][j]
        return maxdiff(0,n-1) >0