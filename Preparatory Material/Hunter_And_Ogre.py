def hide_and_seek(grid):
    n=len(grid)
    for i in range(n):
        if 'A' in grid[i]:
            A=(i,grid[i].index('A'))
        if 'B' in grid[i]:
            B=(i,grid[i].index('B'))
    res=abs(A[1]-B[1])+abs(A[0]-B[0])
    print(B)
    return res
print(hide_and_seek(['A00','000','00B']))
