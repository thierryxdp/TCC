def fatorial(n):
    proximo=1
    fatorial=n
    while n-proximo!=0:
        fatorial=fatorial*(n-proximo)
    proximo=proximo+1
    return fatorial