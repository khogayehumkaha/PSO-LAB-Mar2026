class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

res = removeNthFromEnd(head, 2)
while res:
    print(res.val, end=" ")
    res = res.next