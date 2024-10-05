class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i not in target:
            return -1
        return nums.index(target)
