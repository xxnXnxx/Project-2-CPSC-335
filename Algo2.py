class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def find_duplicate(head):
    slow = fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow.val


head = Node(5)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(7)
head.next.next.next.next = Node(5)

duplicate = find_duplicate(head)
print(duplicate)
