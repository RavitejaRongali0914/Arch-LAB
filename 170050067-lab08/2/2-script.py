import os
import matplotlib.pyplot as plt
os.system("touch out1.txt")
os.system("touch out2.txt")
os.system("touch out3.txt")
files=["out1.txt","out2.txt","out3.txt"]
ans=["./d4-traces/cc1.din","./d4-traces/spice.din","./d4-traces/tex.din"]
for i in range(0,3):
	for j in ("4k","8k","16k","32k","64k","128k","256k","512k"):
		cmd="./dineroIV -l1-usize "+j+" -l1-ubsize 16 -l1-uassoc 2 -l1-uwback a -l1-uwalloc a -l1-uccc -informat d < "+ans[i]+" | grep rate >> "+files[i]
		os.system(cmd)
file1=open("out1.txt","r")
lines=file1.readlines()
a1=[]
b=[4,8,16,32,64,128,256,512]
for line in lines:
    a1.append(float(line.split("\t")[1]))
#print(a1)
plt.figure()
plt.plot(b,a1)
plt.xlabel("Cache size")
plt.ylabel("miss rate")
plt.savefig("q2-cc1.png")
plt.figure()
file1.close()

file2=open("out2.txt","r")
lines=file2.readlines()
a2=[]
for line in lines:
    a2.append(float(line.split("\t")[1]))
plt.figure()
plt.plot(b,a2)
plt.xlabel("Cache size")
plt.ylabel("miss rate")
plt.savefig("q2-spice.png")
plt.figure()
file2.close()

file3=open("out3.txt","r")
lines=file3.readlines()
a3=[]
for line in lines:
    a3.append(float(line.split("\t")[1]))
plt.figure()
plt.plot(b,a3)
plt.xlabel("Cache size")
plt.ylabel("miss rate")
plt.savefig("q2-text.png")
plt.figure()
file3.close()

os.system("rm out1.txt")
os.system("rm out2.txt")
os.system("rm out3.txt")
    # print(line.split(" ")[12])
    # print(line.split(" ")[14])


