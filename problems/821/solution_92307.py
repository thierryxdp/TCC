def fatorial(n):
    
    fatorial=n
    proximo=n-1
    
    while n-proximo<n:
        fatorial=fatorial*(proximo)
        proximo=proximo-1
    return fatorial