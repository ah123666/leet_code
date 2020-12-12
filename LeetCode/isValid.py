"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        strList = list(s)
        if len(strList) % 2 != 0:
            return False
        stackList = []
        p = 0
        while p <= len(strList) - 2:
            stackList.append(strList[p])
            # print(stackList)
            for i in range(p + 1):
                if stackList[i] == strList[p + 1]:
                    if i == p:
                        stackList.pop(-1)
                    else:
                        return False
            stackList.append(strList[p + 1])
            p += 2
            # print(stackList)
        return True

solu = Solution()
s = "{(([]))}"
print(solu.isValid(s))



