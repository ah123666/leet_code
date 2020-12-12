#-*-coding:utf8;-*-
def isHuiWen(x):
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        res = 0
        y = x
        while x:
            res = res * 10 + x % 10
            x = x // 10
        return res == y
        
        
x = 332333333233
print(isHuiWen(x))
