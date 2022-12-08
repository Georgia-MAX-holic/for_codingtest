from itertools import permutations
def solution(k, dungeons):
    MAX = 0
    LIST = list(permutations(dungeons,len(dungeons)))
    
    for permutation in LIST:
        HP =k
        CNT=0

        for insight_per in permutation:
            if insight_per[0]<=HP:
                HP-=insight_per[1]
                CNT+=1 
                
        if MAX<CNT:
            MAX=CNT
                
    return  MAX
