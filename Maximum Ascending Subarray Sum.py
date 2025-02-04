class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur = nums[0]
        res = cur
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                cur+=nums[i]
            else:
                cur = nums[i]
            res = max(cur,res)
        return res
