def uppCons(x):
    n = 0
    string = ''
    while n<len(x):
        if x[n] not in 'aeiouAEIOU':
            x[n]=x.upper[n]
        n = n+1
        
        
    return x