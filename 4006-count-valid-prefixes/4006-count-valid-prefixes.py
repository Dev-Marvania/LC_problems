class Solution:
    def countValidPrefixes(self, s: str) -> int:
        c0 = 0
        c1 = 0
        count = 0
        for c in s:
            if c == '0':
                c0+=1
            else:
                c1+=1

            if abs(c0-c1) <= 1:
                count+=1
        return count