1m 2m 길이를 갖는 선으로 자르려고 함

예를 들어 4m의 네트워크 선이 주어진다면 

1) 1m + 1m + 1m + 1m
2) 2m + 1m + 1m
3) 1m + 2m + 1m 
4) 1m + 1m + 2m
5) 2m + 2m 

의 5가지 방법을 생각할 수 있음, 2와  3과 4의 경우 왼쪽을 기준으로 자르는 위치가 다르면 다른 경우로 생각함 

그렇다면 네트워크 선의 길이가 N 이라면 몇 가지의 자르는 방법을 생각할 수 있는가?

import sys
N = int(sys.stdin.readline())

dy=[0]*(n+1) 
dy[1]=1
dy[2]=2

for i in range(3, n+1):
  dy[i]= dy[i-1] + dy[i-2]

  print(dy[n])
