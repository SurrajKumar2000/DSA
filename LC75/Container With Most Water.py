class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        r = n-1
        l = 0
        max_area = 0
        while l<r:
            w=r-l
            h= min(height[l],height[r])
            a=w*h
            max_area=max(max_area,a)

            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return max_area
            


