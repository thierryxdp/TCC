def fatorial(n):
    proximo=0
    fatorial=0
    while n-proximo!=0:
        fatorial=n*(n-proximo)
    proximo=proximo+1
    return fatorial