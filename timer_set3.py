from time import *
h = int(input('enter the hours : '))
m = int(input('enter the minutes : '))
s = int(input('enter the seconds : '))
y = 0
for b in range(h,-1,-1):
    print(b,end=':')
    if b==(h-1):
        m = 59
    for i in range(m,-1,-1):
        print(i,end=':')
        if i==(m-1) or y==1:
            s = 59
        for j in range(s,-1,-1):
            y = 1
            print(j,end='')
            sleep(.1)
            for k in range(len(str(j))):
                print("\b \b",end='')
        for d in range(len(str(i))+1):
            print("\b \b",end='')
    print("\r",end='')
    for c in range(len(str(b))+4):
        print(" ",end='')
    print("\r",end='')
print("time over")