import numpy as np
c=0 
a=list(map(int,np.random.randint(0,10**9,(10**5,1))))
P=10**7
Q=10**6
while True:
    mx=max(a)
    idx=a.index(mx)
    a[idx]=max(0,a[idx]-P)
    for i in range(1,len(a)):
        if i!=idx:
            a[i]=max(0,a[i]-Q)
    a=[a[i] for i in range(len(a)) if a[i]!=0]
    c=c+1
    if len(a)==0:
        break
print(c)
    

