def viz_of_ivy(A):
    n=len(A)
    m=max(A)
    print('+',end='')
    for _ in range(2*n+1):
        print('-',end='')
    print('\n')
    for j in range(2,m+3):
        print('|',end='')
        for i in range(2,2*n+2):
            if i%2==0:
                print('.',end='')
            else:
                if j<=A[int((i-1)/2)-1]:
                    print('X',end='')
                elif j==A[int((i-1)/2)-1]+1:
                    print('V',end='')
                else:
                    print('.',end='')
        print('\n')
    print('+',end='')
    for _ in range(2*n+1):
        print('-',end='')
viz_of_ivy([3,1,5])

