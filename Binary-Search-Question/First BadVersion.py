class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 0,n
        while(l<r):
            m = (l+r)//2
            if isBadVersion(m):
                m = r
            else:
                l = m+1
        return l
                
