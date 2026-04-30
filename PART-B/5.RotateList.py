class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def rotateRight(head, k):
    if not head:
        return head

    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    k %= length
    if k == 0:
        return head

    tail.next = head
    steps = length - k
    new_tail = head

    for _ in range(steps-1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

res = rotateRight(head, 1)
while res:
    print(res.val, end=" ")
    res = res.next