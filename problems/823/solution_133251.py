def faltante(L):
    k=1
    while k!=len(L)+2:
        if k not in L:
            return k
        k=k+1