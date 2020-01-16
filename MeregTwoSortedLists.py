# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        temp = None
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val <= l2.val:
            temp = l1
            temp.next = self.mergeTwoLists(temp.next, l2)

        else:
            temp = l2
            temp.next = self.mergeTwoLists(l1, temp.next)

        return temp


list1 = ListNode(1)
e2 = ListNode(2)
e3 = ListNode(3)
list1.next = e2
e2.next = e3

list2 = ListNode(10)
e5 = ListNode(20)
e6 = ListNode(40)
list2.next = e5
e5.next = e6

s = Solution()
s.mergeTwoLists(list1, list2)