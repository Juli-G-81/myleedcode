from typing import List




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

    def two_sum(nums, target):
        """这样写更直观，遍历列表同时查字典"""
        dct = {}
        for i, n in enumerate(nums):
            cp = target - n
            if cp in dct:
                return [dct[cp], i]
            else:
                dct[n] = i

    def calTwoNums(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            hashmap[nums[i]] = i
        return[]


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = []
        flag = 0
        while l1 and l2:
            val = l1.val + l2.val + flag
            if val >= 10:
                flag = 1
            else:
                flag = 0
            res.append(val % 10)
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val + flag
            if val >= 10:
                flag = 1
            else:
                flag = 0
            res.append(val % 10)
            l1 = l1.next
        while l2:
            val = l2.val + flag
            if val >= 10:
                flag = 1
            else:
                flag = 0
            res.append(val % 10)
            l2 = l2.next
        if flag:
            res.append(flag)
        l3 = ListNode()
        Head = l3
        l3.val = res[0]
        for i in range(1, len(res)):
            tmp = ListNode()
            tmp.val = res[i]
            l3.next = tmp
            l3 = tmp
        return Head

    # def addTwoNumbers(self, l1, l2):
    #     sum1,sum2 = 0,0
    #     i,j = 1,1
    #     #获取第一个链表代表的数字
    #     while (l1 != None):
    #         sum1 += l1.val * (10 **(i-1))
    #         print("sum1:%d",sum1)
    #         i += 1
    #         l1 = l1.next
    #     #获取第二个链表代表的数字
    #     while (l2 != None):
    #         sum2 += l2.val * (10 ** (j - 1))
    #         j += 1
    #         l2 = l2.next
    #     #将二者相加得到目标数值
    #     a = str(sum1 + sum2)
    #     #生成目标链表
    #     node_lst = []
    #     for i in range(len(a)):
    #         node = ListNode(val=int(a[len(a)- 1 - i]))
    #         node_lst.append(node)
    #     for i in range(len(node_lst) - 1):
    #         node_lst[len(node_lst)- 2 - i].next = node_lst[len(node_lst) - 1 - i]
    #     return node_lst[0]

class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

class Solution4:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


class Solution5:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        print(dp)
        return s[begin:begin + max_len]

class Solution5_2:
    def expandAroundCenter(self, s, left, right):
        print('left: ', left)
        print('s_left', s[left])
        print('right: ', right)
        print('s_right', s[right])

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            print('left: ', left)
            print('s_left', s[left])
            print('right: ', right)
            print('s_right', s[right])
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            print('left1, right1')
            left1, right1 = self.expandAroundCenter(s, i, i)
            print('left2, right2')
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]



if __name__ == '__main__':
    # sol1 = Solution1()
    # a = sol1.calTwoNums(nums=[1,2,3,4,5], target=6)
    # print(a)

    # sol2 = Solution2()
    # pre = ListNode()
    # ListNode_1 = pre
    # a = [1,2,3,4,5,6]
    # ListNode_1.val = a[0]
    # for i in range(1, len(a)):
    #     ListNode_1.next = ListNode(a[i])
    #     ListNode_1 = ListNode_1.next
    #
    # c = sol2.addTwoNumbers(l1=pre, l2=pre)
    # while c:
    #     print(c.val)
    #     c = c.next
    #
    # sol5 = Solution5()
    # a = sol5.longestPalindrome('adadae')
    # print(a)

    sol5 = Solution5_2()
    a = sol5.longestPalindrome('sjsjsjade')
    print(a)
