# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SLinkedList:
    def __init__(self):
        self.headval = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def swap(head):

            if head is None or head.next is None or head.next.next is None:
                return

            swap(head.next.next)

            prev_node = head
            curr_node = prev_node.next
            next_node = curr_node.next
            curr_node.next = next_node.next
            next_node.next = curr_node
            prev_node.next = next_node

        zero_node = ListNode(0)
        zero_node.next = head
        swap(zero_node)
        return zero_node.next


list1 = SLinkedList()
list1.headval = ListNode(1)
e2 = ListNode(2)
e3 = ListNode(3)
e4 = ListNode(4)
e5 = ListNode(5)
e6 = ListNode(6)
list1.headval.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6

o = Solution()
o.swapPairs(list1.headval)
