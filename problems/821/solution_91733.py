def fatorial(n):
    multiplicador = 1
    for c in range(n,0,-1):
        multiplicador *= c
    return multiplicador