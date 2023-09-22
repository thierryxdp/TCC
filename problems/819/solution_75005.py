def filtraMultiplos(L,n):
    while len(L)/n:
        if len(L)/n in L:
            return L