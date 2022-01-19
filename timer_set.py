from time import *
t = int(input())
for i in range(t,-1,-1):
    print(i,end='')
    sleep(1)
    print("\r",end='')
    for j in range(len(str(i))):
        print(" ",end='')
    print("\r",end='')
print("time over")