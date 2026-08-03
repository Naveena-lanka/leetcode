class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        maxSum=float('-inf')
        for num in nums:
            s+=num
            if s>maxSum:
                maxSum=s
            if s<0:
                s=0
        return maxSum