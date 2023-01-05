def solution(number, k):
    LIST =list(number)
    result=[LIST.pop(0)]
    for n in LIST:
        if result[-1] < n:
            while result and result[-1] < n and k>0:
                result.pop()
                k -= 1
            result.append(n)
        elif k == 0 or result[-1] >= n:
            result.append(n)
            
    if k :
        result=result[:-k]
    answer = ''.join(result)

    return answer
