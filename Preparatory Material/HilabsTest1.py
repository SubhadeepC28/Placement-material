t=int(input())
v = [ 10, 230, 559, 1009, 5000, 10000, 1000000000 ]
r = [ 10, 5, 8, 2, 7, 8, 3]
while(t>0):
    ans = 0
    inputs=list(map(int,input().split(" ")))
    a=inputs[0]
    b=inputs[1]
    i=0
    while(a<b):
        while a>v[i]:
            i=i+1
        mini = (min(b,v[i])-a)//r[i]
        ans = ans+ mini
        a = a+mini * r[i]
        if(a < b):
            a += r[i]
            ans=ans+1
        i=i+1
    t=t-1
    print(ans)