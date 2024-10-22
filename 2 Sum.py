class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(n):
            for j in range(i+1,n):
                if (nums[i]+nums[j] == target):            #Brute Force Method
                    return [i,j]
        return [ ] 
