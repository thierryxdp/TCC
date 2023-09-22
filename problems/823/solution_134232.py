def faltante (L):
    """Retorna um número inteiro que pertence ao intervalo [1,N], mas que não 
    pertence à lista de entrada L. list-> int"""
    f = L[0]
    i = 0
    falt = []
    while f == L[i]:
        falt = falt + [L[i],]
        f = int(L[i]) + 1
        i = i+1
    return falt[-1]