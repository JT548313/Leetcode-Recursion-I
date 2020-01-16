# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SLinkedList:
    def __init__(self):
        self.headval = None


class Solution(object):

    def swap(self, prevNode, currNode, nextNode):
        if nextNode:
            currNode.next = nextNode.next
            nextNode.next = currNode

            if prevNode:
                prevNode.next = nextNode

            if currNode and currNode.next:
                self.swap(currNode, currNode.next, currNode.next.next)

        return nextNode

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            head = self.swap(None, head, head.next)

        return head


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

