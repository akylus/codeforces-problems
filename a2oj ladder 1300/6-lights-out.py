lights = [[1,1,1],[1,1,1],[1,1,1]]
ips = []
for i in range(0,3):
    m = input()
    ips.append(m.split())
for i in range(0,3):
    for j in range(0,3):
        if(int(ips[i][j]) % 2 == 1):
            lights[i][j] = 1 - lights[i][j]
            if(i-1 != -1):
                lights[i-1][j] = 1 - lights[i-1][j]
            if(j-1 != -1):
                lights[i][j-1] = 1 - lights[i][j-1]
            if(i+1 < 3):
                lights[i+1][j] = 1 - lights[i+1][j]
            if(j+1 < 3):
                lights[i][j+1] = 1 - lights[i][j+1]
for i in range(0,3):
    for j in range(0,3):
        lights[i][j] = str(lights[i][j])
    str1 = ''.join(lights[i])
    print(str1)