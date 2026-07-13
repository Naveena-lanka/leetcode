class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        a=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if abs(s - target) < abs(a - target):
                    a = s
                if s == target:
                    return s
                elif s < target:
                    l += 1
                else:
                    r -= 1 
        return a
        

            
        