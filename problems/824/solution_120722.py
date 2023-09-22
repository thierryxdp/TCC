def uppCons(x):
    n = 0
    
    while n<len(x):
        if x[n] not in 'aeiouAEIOU':
            consoante = x[n]
            consoante.upper()
        n=n+1
    return x