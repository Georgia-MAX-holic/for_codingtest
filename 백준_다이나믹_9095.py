from collections import deque
import sys

N  =int(sys.stdin.readline())

mem = [0]*11
mem[1]=1
mem[2]=2
mem[3]=4

for i in range(4,11):
    mem[i]=mem[i-3]+mem[i-2]+mem[i-1]
    

for k in range(N):
    m = int(sys.stdin.readline())
    print(mem[m])
    
