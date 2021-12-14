def max_xor(a,arr):
    if len(arr)==0:
        return a
    else:
        m=arr[0]
        for i in range(len(arr)):
            c=a^arr[i]
            print(c)
            if m<=c:
                m=c
        return m
arr=[]
a=8
print(max_xor(8,arr))
