"""
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
说明:

A.length == n + m

4 6 7
2 5 8
"""
from typing import List

class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        # q = 0
        # while q < len(B):
        #     p = 0
        #     if B[q] <= A[p]:
        #         A.insert(p, B[q])
        #     else:
        #         p += 1
        #         while p < len(A):
        #             if B[q] > A[p]:
        #                 p += 1
        #                 if p == len(A):
        #                     A.insert(p, B[q])
        #                     break
        #                 continue
        #             else:
        #                 A.insert(p, B[q])
        #     A.pop(-1)
        #     q += 1
        # for i in range(n):
        #     A.pop(-1)
        A[:] = A[:m]
        A.extend(B)
        A.sort()


s = Solution()
A = [1,2,3,0,0,0]
B = [2,5,6]
s.merge(A, 3, B, 3)
print(A)

