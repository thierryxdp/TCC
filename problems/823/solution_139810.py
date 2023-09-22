def faltante(L):
    ''''''
    N = list(range(len(L)))
    i = 0
    while i <= len(L):
        if N[i] not in L[i]:
            return N[i]