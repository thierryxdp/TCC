def faltante(L):
    i = 0
    n = 1
    while i < len(L) + 1:
        if L[i] != n:
            n = n+1
            i = i+1
            return n