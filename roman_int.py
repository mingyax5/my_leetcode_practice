# leetcode #13 罗马数转换整数
def romanToInt(s:str) -> int:
    dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    n = len(s)
    sum = 0

    for i in range(n - 1):
        if dict[s[i]] < dict[s[i+1]]:
            sum -= dict[s[i]]
        else:
            sum += dict[s[i]]
    return sum + dict[s[-1]]
