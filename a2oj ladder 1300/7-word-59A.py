m = input()
l= 0
u= 0
w = []
w = list(m)
for i in range(0,len(m)):
    if (w[i].islower()):
        l += 1
    else:
       u += 1
if(l>=u):
    print(m.lower())
else:
    print(m.upper())