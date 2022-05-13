class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:

    def ReverseListFunc(head: ListNode, newHead: ListNode):
        while head:
            anext = head.next
            head.next = newHead
            return Solution.ReverseListFunc(anext, head)
        return newHead

    def ReverseList(self, head: ListNode) -> ListNode:
        return Solution.ReverseListFunc(head, None)

if __name__ == '__main__':
    Sol = Solution()
    pre = ListNode(None)
    ListNode_1 = pre
    pre2 = ListNode(None)
    ListNode_2 = pre2
    a = [2, 4, 9, 7]
    b = [5,6,4,9]

    ListNode_1.val = a[0]
    l2 = ListNode(a[1])
    l3 = ListNode(a[2])
    l4 = ListNode(a[3])

    l3.next = l4
    l2.next = l3
    ListNode_1.next= l2


    for i in range(1, len(b)):
        ListNode_2.next = ListNode(b[i])
        ListNode_2 = ListNode_2.next

    c = Sol.ReverseList(ListNode_1)


