def faltante(L):
    x = 0
    N = 1
    faltou = len(L) + 1
    while x < len(L):
        if L[x] != N:
            faltou = N
            break
        N += 1
        x += 1
    return faltou