def solve(B,A):
    

input=open('c:/Users/ABHISHEK/Desktop/eightfold/input.txt')
lines=[]
for r in input.readlines():
    lines.append(r)
T=int(lines.pop(0))
for _ in range(T):
    N=int(lines.pop(0))
    bridge=[]
    for _ in range(N-1):
        bridge.append(list(map(int,lines.pop(0).split(' '))))
    area=list(map(int,lines.pop(0).split(' ')))
    solve(bridge,area)
    


