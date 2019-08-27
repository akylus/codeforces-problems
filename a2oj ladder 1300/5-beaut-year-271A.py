saver = int(input())
flag = 1
while(flag):
    num = saver + 1
    visited = [0,0,0,0,0,0,0,0,0,0]
    while (num): 
        if (visited[int(num % 10)]):
            break
        visited[int(num % 10)] = 1 
        num = int(num/10)
    if (num == 0):
        flag = 0
    else:
        saver += 1
print(saver+1)
