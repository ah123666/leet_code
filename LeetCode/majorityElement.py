"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times = [0] * len(nums)
        count_dict = dict(zip(nums, times))
        for i in range(len(nums)):
            count_dict[nums[i]] += 1
        for key, value in count_dict.items():
            if value > len(nums) // 2:
                return key

        return None

# nums = [1,2,3,4,5]
# s = Solution()
# print(s.majorityElement(nums))

a = [1,2,3,4]
b = [3,4,4,5]
print(dict(zip(a, b)))