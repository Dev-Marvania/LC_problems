class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod_of_digits(n):
            s1 = 1
            while n:
                s1*=n%10
                n//=10
            return s1
        num = n
        while True:
            s1 = prod_of_digits(num)
            if s1%t==0:
                return num
            num+=1
