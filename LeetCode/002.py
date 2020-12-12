#-*-coding:utf8;-*-
#qpy:console

print ("This is console module")
def reverseIntNum(num : int) -> int:
    numList = []
    reverse = 0
    if num <= -(2**31) or num > (2**31 - 1):
        return 0
    elif num < 0:
        num = -num
        i = 10
        while num // i >= 10:
            i = i * 10
        j = i
        while j >= 1: 
            a = num // j
            numList.append(a)
            num = num - a * j
            j = j / 10
        for k in range (len(numList) - 1, -1, -1):
            reverse = reverse + numList[k] * i
            i = i / 10
        reverse = -reverse
        return int(reverse)
    else:
        i = 10
        while num // i >= 10:
            i = i * 10
        j = i
        while j >= 1: 
            a = num // j
            numList.append(a)
            num = num - a * j
            j = j / 10
        for k in range (len(numList) - 1, -1, -1):
            reverse = reverse + numList[k] * i
            i = i / 10
        return int(reverse)


num = -2300
        
print(reverseIntNum(num))
            
        
        
        
        
        
        
    
