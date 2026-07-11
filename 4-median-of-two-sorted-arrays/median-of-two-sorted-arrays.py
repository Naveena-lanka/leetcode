class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=nums1+nums2
        m.sort()
        a=len(m)
        if a%2==0:
            w=(m[a//2-1]+m[a//2])/2
            return w
        else:
            n= m[a//2]
        return n    
    
    
        