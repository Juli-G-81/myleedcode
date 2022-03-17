from typing import List
import pandas

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def two_num(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            hashmap[num] = i
        return []

class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode()
        l3 = pre
        flag = 0
        val = flag + l1.val + l2.val
        flag = 1 if val >= 10 else 0
        l3.val = val % 10
        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            val = flag + l1.val + l2.val
            flag = 1 if val >= 10 else 0
            l3.next = ListNode(val % 10)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + flag
            flag = 1 if val >= 10 else 0
            l3.next = ListNode(val % 10)
            l3 = l3.next
            l1 = l1.next
        while l2:
            val = l2.val + flag
            flag = 1 if val >= 10 else 0
            l3.next = ListNode(val % 10)
            l3 = l3.next
            l2 = l2.next
        while flag:
            print(flag)
            l3.next = ListNode(flag)
            l3 = l3.next
            return pre
        return pre

class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        rk, ans = -1, 0

        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while rk + 1 <n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk += 1
            ans = max(ans, rk + 1 -i)
        return ans

# class Solution4:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # flag = 1
        # while flag:
        #     n1 = [nums1[nums1.length/2 - 1], nums1[nums1.length/2]] if nums1.length % 2 == 0 else [nums1[nums1.length//2]]
        #     n2 = [nums2[nums2.length / 2 - 1], nums2[nums2.length / 2]] if nums2.length % 2 == 0 else [
        #         nums2[nums2.length // 2]]
        #     if n1[-1] <= n2[0]:
        #         nums1 = nums1[nums1.length/2 - 1, ]
        #         nums2 = nums2[0,nums2.length / 2]
        #
        #     if n2[-1] <= n1[0]:
        #         nums2 = nums2[nums2.length / 2 - 1, ]
        #         nums1 = nums1[0,nums1.length / 2]
        #
        #     if (n2[0] <= n1[0] & n2[-1] >= n1[-1]) | (n1[0] <= n2[0] & n1[-1] > n2[-1]):
        #         temp = n1 + n2
        #         a = temp[len(temp)/2-1]+temp[len(temp)/2] if len(temp) %2 ==0 else temp[temp.length//2]
        #         return a
        #
        #     if n1[-1] >= n2[0] & n1[0] <= n2[0] & n1[-1]<= n2[-1]:
        #
        #
        #
        #     if n2[0] >= n1[0] & n2[-1] >= n1[0] & n1[-1] >=n2[-1]:







if __name__ == '__main__':
    # sol1 = Solution1()
    # a = sol1.two_num(nums=[1, 2, 3, 4, 5], target=6)
    # print(a)

    # sol2 = Solution2()
    # pre = ListNode()
    # ListNode_1 = pre
    # pre2 = ListNode()
    # ListNode_2 = pre2
    # a = [2,4,9]
    # b = [5,6,4,9]
    #
    # ListNode_2.val = b[0]
    # ListNode_1.val = a[0]
    # for i in range(1, len(a)):
    #     ListNode_1.next = ListNode(a[i])
    #     ListNode_1 = ListNode_1.next
    # for i in range(1, len(b)):
    #     ListNode_2.next = ListNode(b[i])
    #     ListNode_2 = ListNode_2.next
    #
    # c = sol2.addTwoNumbers(l1=pre, l2=pre2)
    # while c:
    #     print(c.val)
    #     c = c.next

    sol3 = Solution3()
    a = sol3.lengthOfLongestSubstring('fafvvjjajdmakdjidweif')
    print(a)