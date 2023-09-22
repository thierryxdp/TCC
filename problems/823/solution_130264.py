def faltante(L):
    i = 0
    n = 1
    while i < len(L) + 1:
        if L[i] != n:
            i = i+1
            n = n+1
    return n