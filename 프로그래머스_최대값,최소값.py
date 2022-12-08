def solution(s):
    answer = list(map( int , s.split()))
    
    MAX, MIN = str(max(answer)) , str(min(answer))
    result =MIN+" "+MAX
    return result
