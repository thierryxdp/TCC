def fatorial(n):
    """Funcao calcula e retorna o fatorial de um numero(n)
    int,int->int"""
    fatorial=()
    i=0
    while i<n:
        if n[i]>=0:
            fatorial=fatorial*(fatorial-1)
        i=i+1
    return fatorial