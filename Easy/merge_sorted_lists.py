
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert_between(self, left, right, node, head):
        if left is None:
            node.next = right
            return node
        elif right is None:
            left.next = node
            node.next = None
            return head
        else:
            left.next = node
            node.next = right
        return head

    def mergeTwoLists(self, list1, list2) -> ListNode:
        head = list2
        curr = list1
        prev = None
        right = head
        while curr is not None:
            while right is not None and curr.val > right.val:
                prev = right
                right = prev.next
            temp = curr.next
            head = self.insert_between(prev, right, curr, head)
            curr = temp
            right = head
        return head

    def is_equal(self, list1, list2) -> bool:
        head1 = list1
        head2 = list2
        while True:
            if head1.val != head2.val:
                return False
            elif head1.next is None and head2.next is not None:
                return False
            elif head2.next is None and head1.next is not None:
                return False
            elif head1.next is None and head2.next is None:
                return True
            else:
                head1 = head1.next