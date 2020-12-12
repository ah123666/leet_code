"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        list_a = list(a)
        list_b = list(b)
        for i in range(len(list_a)):
            list_a[i] = int(list_a[i])
        for i in range(len(list_b)):
            list_b[i] = int(list_b[i])
        while len(list_a) != len(list_b):
            if len(list_a) < len(list_b):
                list_a.insert(0, 0)
            elif len(list_a) > len(list_b):
                list_b.insert(0, 0)

        list_c = []
        for i in range(len(list_a)):
            list_c.append(list_a[i] + list_b[i])

        p = len(list_c) - 1
        while p >= 0:
            if list_c[p] > 1:
                list_c[p] -= 2
                if p - 1 >= 0: 
                    list_c[p - 1] += 1
                else:
                    list_c.insert(0, 1)
            p -= 1

        for i in range(len(list_c)):
            list_c[i] = str(list_c[i])

        result = ''.join(list_c)
        return result







a = '11'
b = '111'
print(bin(int(a, 2) + int(b, 2))[2:])



