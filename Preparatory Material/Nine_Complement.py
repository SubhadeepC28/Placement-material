arr=[616,3922,1185,560]
queries=[[1,0,2,0,2],[1,1,2,1,2],[2,0,3,0,3],[1,0,2,0,2],[2,0,0,0,1]]
arr=list(map(str,arr))
N=4
def nine_complement(N,s,e,number):
    if len(number)<N:
        while True:
            number='0'+number
            if len(number)==N:
                break
    for i in range(N-1-e,N-s):
        if(number[i] != '.'):
            a = 9 - int(number[i])
            number = (number[:i] +
                     str(a) + number[i + 1:])
    return str(int(number))
def adder(N,s,e,number):
    if len(number)<N:
        while True:
            number='0'+number
            if len(number)==N:
                break
    s=0
    for i in range(N-1-e,N-s):
        if(number[i] != '.'):
            a =  int(number[i])
            s=s+a
    return s
for q in queries:
    type=q[0]
    l=q[1]
    r=q[2]
    s=q[3]
    e=q[4]
    if type==1:
        temp_nums=arr[l:r+1]
        arr[l:r+1]=[nine_complement(N,s,e,t) for t in temp_nums]
        print(arr)
    if type==2:
        temp_nums=arr[l:r+1]
        s=0
        for t in temp_nums:
            s=s+adder(N,s,e,t)
        print(s)

