class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(x):
            if len(sol) == k:
                res.append(sol[:])
                return

            if x < k - len(sol):
                return

            # Don't take x
            backtrack(x - 1)

            # Take x
            sol.append(x)
            backtrack(x - 1)
            sol.pop()

        backtrack(n)
        return res