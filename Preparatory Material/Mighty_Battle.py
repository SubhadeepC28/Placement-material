def max_xor(a,arr):
    if len(arr)==0:
        return a
    else:
        m=arr[0]
        for i in range(len(arr)):
            c=a^arr[i]
            if m<=c:
                m=c
        return m
def solver(N,A,B):
    A_dead=[]
    B_dead=[]
    for i in range(N):
        X=max_xor(A[i],A_dead)
        Y=max_xor(B[i],B_dead)
        if X>Y:
            # print(B)
            b=B[i]
            B_dead.append(b)
        elif X<Y:
            # print(A)
            a=A[i]
            A_dead.append(a)
    return len(B)-len(B_dead)
print(solver(4,[4, 8, 6, 7],[2, 8, 10, 5]))

