"""
给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：

countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1 
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-and-say
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        # res = ["1"]                 # 当前输出外观数列
        # for i in range(n - 1):
        #     p = 0                   # p初始化为0，q初始化为1，遍历当前输出外观res以获得下一输出
        #     q = 1                   # q向右移动，直至q指向的值不等于p指向的值，此时q-p为p所指向的值的重复个数
        #     tmp = []                # 用于存储下一输出外观数列
        #     while q <= len(res):
        #         if q == len(res):   # 特殊边界位置的处理：当q == len(res)刚好溢出时
        #             tmp.extend([str(q - p), res[p]])
        #         elif res[q] != res[p]:
        #             tmp.extend([str(q - p), res[p]])
        #             p = q
        #         q += 1
        #     res = tmp
        # return "".join(res)

        result = ["1"]
        for i in range(n - 1):
            p = 0
            cnt = 1
            tmp = []
            while p < len(result):
                if p + 1 == len(result):
                    tmp.extend([str(cnt), result[p]])
                elif result[p + 1] == result[p]:
                    cnt += 1
                elif result[p + 1] != result[p]:
                    tmp.extend([str(cnt), result[p]])
                    cnt = 1
                p += 1
            result = tmp
        return "".join(result)


s = Solution()
n = 30
print(s.countAndSay(n))
