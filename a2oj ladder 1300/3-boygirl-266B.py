m = input()
ips = []
ips.append(m.split())
t = int(ips[0][1])
ip = input()
for i in range (0,t):
    ip = ip.replace('BG','GB')
print(ip)
