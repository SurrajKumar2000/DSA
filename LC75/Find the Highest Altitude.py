class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0
        current = 0
        for i in range (len(gain)):
            current+=gain[i]
            high = max(high,current)
        return high   
