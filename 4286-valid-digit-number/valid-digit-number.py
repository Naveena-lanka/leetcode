class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        str1=list(str(n))
        if str1[0]!=str(x) and str(x) in str1:
            return True
        else:
            return False