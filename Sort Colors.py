class Solution:
    def sortColors(self, nums: List[int]) -> None:

        counts = [0,0,0]
        for colors in nums:
            counts[colors]+=1

        r,w,b = counts
        nums[:r] = [0] * r
        nums[r:r+w] = [1] * w
        nums[r+w:] = [2] * b
