def faltante(L):
    ''''''
    N = list(range(1, len(L)+2))
    i = 0
    while i <= len(L):
        if N[i] not in L:
            return N[i]
        i += 1