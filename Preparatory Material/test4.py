from itertools import combinations
cards=[ i for i in range(10)]*2
l=list(combinations(cards,5))
print(len(l))

print(list(combinations([0,2,0,2,0,2,0,2],3)))  
