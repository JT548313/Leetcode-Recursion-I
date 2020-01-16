# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SLinkedList:
    def __init__(self):
        self.headval = None


class Solution(object):
    def __init__(self):
        self.master = None

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        if head.next.next is not None:
            self.reverseList(head.next)
        else:
            self.master = head.next

        prev_node = head
        curr_node = head.next
        prev_node.next = curr_node.next
        curr_node.next = prev_node


        return self.master


list1 = SLinkedList()
list1.headval = ListNode(1)
# e2 = ListNode(2)
# e3 = ListNode(3)
# e4 = ListNode(4)
# e5 = ListNode(5)
# e6 = ListNode(6)
# list1.headval.next = e2
# e2.next = e3
# e3.next = e4
# e4.next = e5
# e5.next = e6

o = Solution()
o.reverseList(list1.headval)