class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open,add = 0,0
        if not s:
            return 0
        for c in s:
            if c == '(':
                open+=1
            if c == ')':
                if open:
                    open-=1
                else:
                    add+=1
        return add+open