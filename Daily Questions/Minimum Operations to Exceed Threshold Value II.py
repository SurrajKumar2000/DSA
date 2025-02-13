class Solution:
    def minOperations(self, h: List[int], k: int) -> int:
        heapify(h)
        res = 0
        while h[0] < k:
            heapreplace(h, heappop(h)*2 + h[0])
            res += 1
        
        return res
