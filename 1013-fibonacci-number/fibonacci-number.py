class Solution:
    def fib(self, x: int) -> int:
        memo={0:0,1:1}
        def fib(x):
            if x in memo:
                return memo[x]
            else:
                memo[x]=self.fib(x-1)+self.fib(x-2)
                return memo[x]
        return fib(x)            