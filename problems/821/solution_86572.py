def fatorial(n):
    """recebe um número e calcula o fatorial dele;int->int"""
    fatn=1
    i=1
    while i<n+1:
        fatn=i*fatn
        i=i+1
    return fatn