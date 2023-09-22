def uppCons(x):
    n = 0
    
    while n<len(x):
        if x[n] != 'a' and 'e' and 'i' and 'o' and 'u':
            consoante = x[n]
            consoante.upper()
        n=n+1
    return x