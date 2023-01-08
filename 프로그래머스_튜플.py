def solution(s):
    
    LIST = s[1:-1].split("}")
    LIST.sort(key=len)
    LIST = LIST[1:]
    result=[]
    solve = []
    for i in LIST :
        if i[0]=="{":
            result.append(i[1:])
            
        elif i[0]==",":
            result.append(i[2:])
        
        
    if len(result)==1:
        return [int(result[0])]
    
    for k in result:
        for j in k.split(","):
            if int(j) not in solve:
                solve.append(int(j))
    
    return solve
