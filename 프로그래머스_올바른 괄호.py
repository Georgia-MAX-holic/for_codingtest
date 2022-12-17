from collections import deque 

def solution(s):
    S = list(s)
    LIST = deque()
    
    for i in S:
        if i =="(":
            LIST.append(i)
        else:
            try:
                LIST.pop()
            except:
                return False

    if len(LIST)==0:
        return True
    else:
        return False
