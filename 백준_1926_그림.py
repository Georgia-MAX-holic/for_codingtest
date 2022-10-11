from collections import deque 

n,m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,cnt):
    graph[x][y]=0
    queue = deque()
    queue.append([x,y])
    cnt=1 
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            
            if -1<nx<n and -1<ny<m and graph[nx][ny] ==1 :
                graph[nx][ny]= 0
                queue.append([nx,ny])
                cnt+=1
                
    return cnt 

result = []
        
for i in range(n):
    for j in range(m):
        if graph[i][j] ==1 :
            result.append(bfs(i,j,0))
            
if len(result) == 0:
    print(0,0,sep='\n')

else :
    print(len(result))
    print(max(result))
