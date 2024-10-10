class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if i not in target:
            return -1
        return nums.index(target)
