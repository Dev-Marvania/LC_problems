class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n%2 == 0:
            return True

        def maxdiff(i,j):
            if i==j:
                return nums[i]
            return max(nums[i]-maxdiff(i+1,j),nums[j]-maxdiff(i,j-1)) 

        return maxdiff(0,n-1) >=0