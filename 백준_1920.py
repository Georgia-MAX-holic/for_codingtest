####
#N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

#첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
#다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

#M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

#input  
#5
#4 1 5 2 3
#5
#1 3 7 9 5


#output

#1
#1
#0
#0
#1

# result


N1 = int(input())
LIST1 = list(map(int,input().split()))
N2 = int(input())
LIST2 = list(map(int, input().split()))

LIST1.sort()

def Count(luka):
    

    L = 0
    R = (N1-1)
    
    while L <=R:
        mid = (L+R)//2
        if LIST1[mid] == luka :
        
            return True
        
        elif LIST1[mid] < luka :
            L= mid+1
            
        elif LIST1[mid]> luka:
            R=mid-1


for i in range(N2):
    if Count(LIST2[i]):
        print(1)
        
    else:
        print(0)
