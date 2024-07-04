# leetcode #28 字符串第一项匹配

def strStr(haystack: str, needle: str) -> int:
    if len(haystack) == 1:
        if haystack == needle:
            x = 0
        else: 
            x = -1
    else:
        for i in range(0,len(haystack) - 1,1):
            if needle == haystack[i:i+len(needle)]:
                x = i
                break
            if needle == haystack[-1]:
                x = len(haystack) - 1
                break
            else:
                x = -1
    return x
