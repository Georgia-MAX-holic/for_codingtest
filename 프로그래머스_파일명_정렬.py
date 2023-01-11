def solution(files):
    tmp = []
    head, number, tail = '', '', ''
    
    for file in files:       
        for i in range(len(file)):
            if file[i].isdigit():     
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):    
                    if not number[j].isdigit():  # 숫자인지 아닌지 구별해줌
                        tail = number[j:]
                        number = number[:j]
                        break
                        
                tmp.append([head, number, tail])
                head, number, tail = '', '', ''
                break

    tmp = sorted(tmp, key=lambda x:(x[0].lower(), int(x[1])))

    return [''.join(i) for i in tmp]
