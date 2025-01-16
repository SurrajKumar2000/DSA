class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Max_Candies = max(candies)

        return [(curNum+extraCandies>=Max_Candies) for curNum in candies]        
