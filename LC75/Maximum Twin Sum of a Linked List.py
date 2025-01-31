
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        cur = slow
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head2 = prev
        max_sum = 0
        while head2:
            max_sum = max(max_sum, head.val+head2.val)
            head = head.next
            head2 = head2.next
        return max_sum

