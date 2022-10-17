N = int(input())
LIST = []

Height_result = 0
width_result = 0

def RESULT_width(List):
  cnt = 0
  result= 0

  for k in range(N):

      for j in range(N):
        if List[k][j] == ".":
           cnt+=1
    
        elif LIST[k][j] =="X":
          if cnt>=2 :
            result+=1
    
          cnt =0

      if cnt>=2 :
        result+=1
  
      cnt =0
  return result

def RESULT_height(List):
  cnt = 0
  result= 0

  for j in range(N):

      for k in range(N):
        if List[k][j] == ".":
           cnt+=1
    
        elif LIST[k][j] =="X":
          if cnt>=2 :
            result+=1
    
          cnt =0

      if cnt>=2 :
        result+=1
  
      cnt =0
  return result





for i in range(N):
  LIST.append(list(map(str,input())))




      

print(RESULT_width(LIST),RESULT_height(LIST))
