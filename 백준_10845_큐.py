

from collections import deque
import sys
LIST = deque([])
N = int(sys.stdin.readline())


for _ in range(N):
    Command=sys.stdin.readline().split()
    
    if Command[0]=="push":
        LIST.append(Command[1])
        
    elif Command[0] == "front":
        if len(LIST)==0:
            print(-1)
            
        else: 
            front = LIST[0]
            print(front)
    elif Command[0] == "back":
        if len(LIST)==0:
            print(-1)
            
        else:
            back = LIST[-1]
            print(back)
            
    elif Command[0] =="size":
        print(len(LIST))
        
    elif Command[0] =="empty":
        if len(LIST)==0:
            print(1)
        else :
            print(0)
            
    elif Command[0] =="pop":
        
        if len(LIST)==0:
            print(-1)
            
        else :
            POP_LEFT = LIST.popleft()
            print(POP_LEFT)
