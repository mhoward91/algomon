class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(n) time, O(1) space
    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        return prev

    def other_reverse_list(self, head: ListNode) -> ListNode:
        dummy_node = ListNode()
        curr = head
        while curr:
            nxt = curr.next
            curr.next = dummy_node.next

            dummy_node.next = curr
            curr = nxt

        return dummy_node.next
