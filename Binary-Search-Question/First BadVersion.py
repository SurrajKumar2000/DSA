class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 0,n
        while(l<r):
