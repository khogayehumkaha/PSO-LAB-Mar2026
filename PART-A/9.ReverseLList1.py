class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def reverseList(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

rev = reverseList(head)
while rev:
    print(rev.val, end=" ")
    rev = rev.next