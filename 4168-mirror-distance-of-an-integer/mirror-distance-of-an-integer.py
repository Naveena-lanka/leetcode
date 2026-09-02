class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp=n
        rnum=0
        while n>0:
            d=n%10
            rnum=rnum*10+d
            n//=10
        return abs(temp-rnum)    
        