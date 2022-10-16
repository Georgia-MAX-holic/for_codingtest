import math

N = int(input())


def isPrime(x): 
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


    

        
for k in range(N,10000000):
    if k == 1 :
        continue
    
    if isPrime(k) == True:
        if str(k) == str(k)[::-1]:  # 앞에서부터 읽은놈과 뒤에서 읽은놈이 같다면 
            print(k)
            break
            
            
            
