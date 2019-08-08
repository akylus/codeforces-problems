n = int(input())
equi = 0
flag = 0
svectors = []
vectorrow = []
vectorrow2 = []
vectorsint = []
for i in range (0,n):
	m = input()
	svectors.append(m.split())
for i in range (0,n):
    for item in svectors[i]:
        try:
            vectorrow.append(int(item))
        except ValueError as e:
            vectorrow.append(item)
    vectorrow2 = vectorrow.copy()
    vectorrow.clear()
    vectorsint.append(vectorrow2)
for k in range (0,len(vectorsint[0])):
    for i in range (0,n):
        equi += vectorsint[i][k]
    if (equi != 0):
        flag = 1
        break
    equi = 0
if (flag == 0):
    print ("YES")
else:
    print ("NO")
