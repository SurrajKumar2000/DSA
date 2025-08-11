class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            while not self.isAlNum(s[l]) and l<r:
                l+=1
            while not self.isAlNum(s[r]) and r>l:
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
    def isAlNum(self,c):
        return ('a'<=c<='z' or 'A'<=c<='Z' or '0'<=c<='9')

