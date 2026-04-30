class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def reverseBetween(head, left, right):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left-1):
        prev = prev.next

    curr = prev.next
    for _ in range(right-left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

res = reverseBetween(head, 2, 3)
while res:
    print(res.val, end=" ")
    res = res.next