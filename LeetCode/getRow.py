"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        before = [1, 1]
        i = 0
        while i < rowIndex - 1:
            result = [1, 1]
            for j in range(len(before) - 1):
                result.insert(-1, before[j] + before[j + 1])
            before = result
            i += 1
        return result


s = Solution()
print(s.getRow(4))
