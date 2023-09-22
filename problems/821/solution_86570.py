def fatorial(n):
    """recebe um número e calcula o fatorial dele;int->int"""
    fatn=1
    i=1
    while 0<i<n+1:
        fatn=i*fatn
    return fatn