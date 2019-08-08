m = input()
answer = []
flag = 0
i = 0
while(i < len(m)):
    if(m[i] == '.'):
        answer.append(0)
        flag += 1
    elif(m[i] == '-'):
        if(i+1 < len(m)):
            if(m[i+1] == '.'):
                answer.append(1)
            elif(m[i+1] == '-'):
                answer.append(2)
            flag += 1
            i += 1
    i += 1
answer = ''.join(str(i) for i in answer)
print(answer)
