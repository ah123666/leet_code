"""
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # sentinel = ListNode(0)
        # sentinel.next = head # 设置哨兵节点

        # prev, cur = sentinel, head # 前继节点，当前节点

        # while cur: # 循环终止条件
        #     if cur.val == val:
        #         prev.next = cur.next  # 删除节点
        #     else:
        #         prev = cur # 前继指针滑动
        #     cur = cur.next # 当前指针滑动

        # return sentinel.next
        if not head:
            return
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head


def makeList():
    head = ListNode(0)
    a = ListNode(5)
    head.next = a
    for i in range(4, 0, -1):
        b = ListNode(i)
        b.next = head.next
        head.next = b
    return head


def makeList2():
    head = ListNode(0)
    tail = ListNode(-1)
    a = ListNode(1)
    head.next = a
    tail.next = a
    for i in range(2, 6, 1):
        b = ListNode(i)
        tail.next.next = b
        tail.next = b
    return head


def makeMyList():
    tail = ListNode(-1)
    length = int(input("输入长度："))

    val = float(input("输入头结点的值："))
    head = ListNode(val)

    if length < 2:
        return head

    val = float(input("输入节点1的值："))
    a = ListNode(val)

    head.next = a
    tail.next = a
    for i in range(length - 2):
        val = float(input("输入节点" + str(i + 2) +"的值："))
        b = ListNode(val)
        tail.next.next = b
        tail.next = b
    return head


def showList(head):
    if head == None:
        return
    else:
        print(head.val)
        showList(head.next)

if __name__ == '__main__':
    head = makeMyList()
    showList(head)
    s = Solution()
    head = s.removeElements(head, 5)
    print("after remove:")
    showList(head)

