def uppCons(x):
    n = 0
    letra = x[n]
    while n<len(x):
        if letra not in 'aeiouAEIOU':
            letra.upper(1)
           
        n=n+1
    return x