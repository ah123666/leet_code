def romanToInt(s:str)->int:
    numDist = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "Z":2000}
    strList = list(s)
    result = 0
    for i in range(0, len(strList) - 1):
        if numDist[strList[i]] < numDist[strList[i + 1]]:
            result += numDist[strList[i + 1]] - numDist[strList[i]]
            strList[i] = "Z"
            strList[i + 1] = "Z"

    for i in range(0, len(strList)):
        if strList[i] == "Z":
            continue
        result += numDist[strList[i]]

    return result
    # a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}        
    # ans=0        
    # for i in range(len(s)):            
    #     if i<len(s)-1 and a[s[i]]<a[s[i+1]]:                
    #         ans-=a[s[i]]
    #     else:
    #         ans+=a[s[i]]
    # return ans

print(romanToInt("IX"))