import collections


def solution(k, tangerine):
    cnt=0
    POP=0
    luka=collections.Counter(tangerine) # 딕셔너리 형식으로 카운트 
    LUKA=sorted(luka.values()) # 값만 반환
    
    for i in range(len(LUKA)):
        POP+=LUKA.pop()
        cnt+=1
        if POP>=k:     
            return cnt
