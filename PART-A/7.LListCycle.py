class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


head = ListNode(1)
node2 = ListNode(2)
head.next = node2
node2.next = head

print(hasCycle(head))