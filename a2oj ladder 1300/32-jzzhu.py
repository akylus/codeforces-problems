m = input()
mandn = m.split()
for i in range (0,len(mandn)):
    mandn[i] = int(mandn[i])
num = mandn[1]
n = input()
list1 = n.split()
for i in range (0,len(list1)):
    list1[i] = int(list1[i])
modlist = list1.copy()
count = 1
while(count):
    slist = modlist.copy()
    slist.sort()
    if(slist[-1] <= num):
        for i in range(len(modlist)-1,-1,-1):
            if(modlist[i]!= 0):
                final = i+1
                count = 0
                break
    elif(slist[-1] == 0):
        final = len(modlist)
        count = 0
    for i in range(0,len(list1)):
        rem = modlist[i] - num
        if(rem < 0):
            modlist[i] = 0
        else:
            modlist[i] = rem
print(final)