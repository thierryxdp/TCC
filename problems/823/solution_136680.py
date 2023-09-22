def faltante(L):
    n = inst(len(L)) + 1
    i = 1
    while i<n:
        if i not in L:
            return i