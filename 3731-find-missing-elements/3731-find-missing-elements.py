class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l1 = []
        n1 = set(nums)
        for i in range(min(n1),max(n1)):
            if i==0:
                continue
            if i not in n1:
                l1.append(i)
        return l1