class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #递归
    def printListFromTailToHead(self, listNode):
        res = []

        def printListnode(listNode):
            # write code here
            if listNode:
                printListnode(listNode.next)  # 先递归到最后一层
                res.append(listNode.val)  # 添加值，退出函数，返回到上一层函数中的这行，继续添加值

        printListnode(listNode)
        return res