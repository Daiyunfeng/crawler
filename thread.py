import threading
import time


def target(n):
    n = int(n)
    num = [0 for x in range(0, n)]
    for i in range(2,n):
        if(num[i]==0):
            print(i,end=" ")
            for j in range(2,int(n/i)):
                num[i*j]=1
    print()
count = 100
while(count!=0):
# n = input("n:")
    count-=1
    n=10000
    t = threading.Thread(target=target,args=(n,))
    t.setDaemon(True)
    t.start()
    #t.join()
