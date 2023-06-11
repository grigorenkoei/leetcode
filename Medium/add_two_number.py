class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        digit = l1.val + l2.val
        head = ListNode(digit % 10)
        node = head
        transfer = digit // 10
        l1 = l1.next
        l2 = l2.next
        while l1 is not None or l2 is not None or transfer != 0:
            if l1 is not None:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0

            if l2 is not None:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
            sum = num1 + num2
            digit = (sum + transfer) % 10
            transfer = (sum + transfer) // 10
            node.next = ListNode(digit)
            node = node.next
        return head
