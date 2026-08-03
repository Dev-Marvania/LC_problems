class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        if n%2 == 0:
            return True

        def maxdiff(i,j):
            if i==j:
                return piles[i]
            return max(piles[i]-maxdiff(i+1,j),piles[j]-maxdiff(i,j-1)) 

        return maxdiff(0,n-1) >0