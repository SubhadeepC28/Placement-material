def complement(N,s,e,number):
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
print(complement(4,2,3,'616'))
