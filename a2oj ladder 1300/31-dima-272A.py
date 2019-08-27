num = int(input())
count = 0
ppl = num + 1
y=input()
x = y.split()
for i in range (0,num):
	x[i] = int(x[i])
total = sum(x)
for i in range(1,6):
	if((total+i) % ppl != 1):
		count += 1
print(count)

