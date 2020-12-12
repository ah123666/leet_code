"""
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。

返回重复了 N 次的那个元素。

 

示例 1：

输入：[1,2,3,3]
输出：3
示例 2：

输入：[2,1,2,5,3,2]
输出：2
示例 3：

输入：[5,1,5,2,5,3,5,4]
输出：5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # for _, num in enumerate(A):
        #     if A.count(num) > 1:
        #         return num
        # return -1

        a = A[0]
        for _, num in enumerate(A, start=1):
            if num == a:
                return num
            else:
                a = num
        return -1

solu = Solution()
A = [2,1,2,5,3,2]
print(solu.repeatedNTimes(A))



