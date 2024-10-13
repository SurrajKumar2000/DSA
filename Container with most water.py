class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0 
        r = n - 1
        max_area = 0
        while(l<r):
            m = (l+r)//2
            w = r - l
            h = min(height[l],height[r])
            max_area = max(max_area,a)
            if (height[l]<height[r]):
                l+=1
            else:
                r-=1
        return max_area
