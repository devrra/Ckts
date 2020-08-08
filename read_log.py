import matplotlib.pyplot as plt

file = open("D:/Works/LtspiceCkts/CurrentMirror/simple_CS.log",'r')
content = file.readlines()

data = []
d = -1

r = len(content)
print(r)

R = []
for i in range(r):
    wrds = content[i].split("\t")
    if "i(r)\n" in wrds:
        R.append(i+1)
        #print(wrds)
    if "v(d)\n" in wrds:
        R.append(i+1)

for t in R:
    data.append([])
    d = d+1
    while True:
        wrds = content[t].split("\t")
        num = float(wrds[-1].split("\n")[0])
        data[d].append(num)
        t = t+1
        if len(content[t])==1:
            break

print(data[0])
print(data[1])
#plt.plot(data[1],data[0],'-o')
#plt.show()
#print(data)
