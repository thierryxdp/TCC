def fatorial(n):
    """
    calcula o fatorial do numero dado
    """
    f=list(range(n+1))
    f.remove(0)
    i=0
    fatorial=1
    while i<len(f):
        fatorial=fatorial*f[i]
        i+=1
    return fatorial