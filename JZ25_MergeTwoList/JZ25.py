class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def ReverseListFunc(head: ListNode, newHead: ListNode):
        while head:
            anext = head.next
            head.next = newHead
            return Solution.ReverseListFunc(anext, head)
        return newHead


    def MergeListFunc(self, l1: ListNode, l2: ListNode):
        aL1Next = 

    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:

        Solution.MergeListFunc(pHead1, pHead2)
