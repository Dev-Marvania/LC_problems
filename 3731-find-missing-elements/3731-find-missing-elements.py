class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l1 = []
        for i in range(min(nums),max(nums)):
            if i==0:
                continue
            if i not in nums:
                l1.append(i)
        return l1