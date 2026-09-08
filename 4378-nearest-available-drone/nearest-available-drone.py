class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        dx,dy=target
        idx=-1
        best=float('inf')
        for i, (x,y,r) in enumerate(drones):
            dist=abs(x-dx)+abs(y-dy)
            if dist<=r and dist<best:
                best=dist
                idx=i
        return idx              