# 1370. 上升下降字符串
# 给你一个字符串 s ，请你根据下面的算法重新构造字符串：

# 从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
# 从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
# 重复步骤 2 ，直到你没法从 s 中选择字符。
# 从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
# 从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
# 重复步骤 5 ，直到你没法从 s 中选择字符。
# 重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
# 在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

# 请你返回将 s 中字符重新排序后的 结果字符串 。

class Solution:

    def sortString(self, s: str) -> str:

        result = ''
        while s:
            res_s = s
            min_s = min(res_s)
            result += min_s
            res_s = res_s.replace(min_s, "")
            s = s[:s.index(min_s)] + s[s.index(min_s)+1:]
            print("s:", s)
            print("min_s:", min_s)
            print("res_s:", res_s)
            print("result:", result)
            print("\n")

            while res_s:
                new_min_s = min(res_s)
                if new_min_s > min_s:
                    result += new_min_s
                    min_s = new_min_s
                    res_s = res_s.replace(min_s, "")
                    s = s[:s.index(min_s)] + s[s.index(min_s)+1:]
                    print("s:", s)
                    print("min_s:", min_s)
                    print("res_s:", res_s)
                    print("result:", result)
                    print("\n")
                else:
                    break

            print("\n"*3)
            print("*"*20)
            print("\n"*3)
            if not s:
                break
            res_s = s
            max_s = max(res_s)
            result += max_s
            res_s = res_s.replace(max_s, "")
            s = s[:s.index(max_s)] + s[s.index(max_s)+1:]
            print("s:", s)
            print("max_s:", max_s)
            print("res_s:", res_s)
            print("result:", result)
            print("\n")

            while res_s:
                new_max_s = max(res_s)
                if new_max_s < max_s:
                    result += new_max_s
                    max_s = new_max_s
                    res_s = res_s.replace(max_s, "")
                    s = s[:s.index(max_s)] + s[s.index(max_s)+1:]
                    print("s:", s)
                    print("max_s:", max_s)
                    print("res_s:", res_s)
                    print("result:", result)
                    print("\n")
                else:
                    break

        return result

solu = Solution()
s1 = "aaaabbbbcccc"
s2 = solu.sortString(s1)
print(s2)





# def str_del_element(s,element):
#     index = s.index(element)
#     return s[:index] + s[index+1:]

# s1 = 'abc'
# print(s1)
# print(len(s1))
# s2 = str_del_element(s1, "b")
# print(s2)
# print(len(s2))
