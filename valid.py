# leetcode #20 有效括号
'''
def isValid(s: str) -> bool:
    flag = 0
    for i in range(0,len(s)-1,2):
        if (s[i] == "(" and s[i+1] == ")") or (s[i] == "[" and s[i+1] == "]" ) or (s[i] == "{" and s[i+1] == "}"):
            flag = True
        else:
            flag = False
    return flag
            
print(isValid("(]"))
'''

def isValid(s:str) -> bool:
    dict={"(" : ")" , "[" : "]" , "{" : "}"}
    stack = ["?"]
    for x in s:
        if x in dict:
            stack.append(x)
        elif dict[stack.pop()] != x: 
            return False 
    return len(stack) == 1

print(isValid("()[]{}"))