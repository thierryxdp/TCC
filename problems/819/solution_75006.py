def filtraMultiplos(L,n):
    pos=[0]
    while len(pos)/n:
        if len(pos)/n in L:
            pos=pos+[1]
            return L