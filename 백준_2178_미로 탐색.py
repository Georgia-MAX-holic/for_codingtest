import sys
from collections import deque

N, M = map( int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))
# 너비 우선
def bfs (x,y):
    dx = [-1, 0 , 1, 0 ]
    dy = [0 , 1, 0 , -1]
    # 이동할 네 가지 방향 정의 
    queue = deque()
    queue.append((x,y))
    # 데크
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 4방위 전부 탐색 
            if nx<0 or nx >= N or ny <0 or ny>=M:
                continue
            
            if graph[nx][ny] ==0 :
                continue
            
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y] +1 
                queue.append((nx,ny))
            # 만약 1일 경우 진행 
            # 이전 모두 더한값 + 1 , 그리고 그걸 데크에 입력 
            # 데크에 입력된걸 다시 탐색 
    return graph[N-1][M-1]

print(bfs(0,0))
