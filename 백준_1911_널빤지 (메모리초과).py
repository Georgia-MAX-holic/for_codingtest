from collections import deque

N , K  =map(int, input().split())
LIST = deque()
LIST2 = deque()
cnt=0
for i in range(N):
    A, B = map (int , input().split())
    

    if len(LIST2)<B:
        for _ in range(B-len(LIST2)):
            LIST2.append(1)
    
    
    LIST.append((A,B))

    for m in range(A,B):
        LIST2[m]=0
        

while LIST2:
    
    Q = LIST2.popleft() 
    if Q ==0:
    
        LIST2.popleft()
        LIST2.popleft()
        
        cnt+=1
        
        
print(cnt)

        
