from time import *
m = int(input('enter the minutes : '))
s = int(input('enter the seconds : '))
for i in range(m,-1,-1):
    print(i,end=':')
    if i==(m-1):
        s = 59
    for j in range(s,-1,-1):
        print(j,end='')
        sleep(1)
        for k in range(len(str(j))):
            print("\b \b",end='')
    print("\r",end='')
    for a in range(len(str(i))+2):
        print(" ",end='')
    print("\r",end='')
print("time over")