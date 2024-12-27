class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if (i%15 == 0):
                out = "FizzBuzz"
            elif (i%3 == 0):
                out = "Fizz"
            elif i%5 == 0:
                out = "Buzz"
            else: 
                out = (str(i))
            ans.append(out)
        return ans
