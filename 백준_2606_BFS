from collections import deque

N = int(input())
K = int(input())
graph = {}
for _ in range(K):
    A ,B = map(int, input().split())
    if A in graph:
        graph[A].append(B)
        
    else :
        graph[A]=[B]
        
    
    if B in graph:
            graph[B].append(A)
    else:
        graph[B] = [A]
        
    
        

queue = deque([1])
cnt = 0 
visited = [1]
while queue :
    Q = queue.popleft()
    
    if Q in graph:
        for i in graph[Q]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                cnt+=1


print(cnt)
