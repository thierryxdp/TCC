def faltante(L):
    i=0
    t=range(1,L[len(L)-1])
    while i<len(t):
        if t[i] not in L:
            return t[i]
        i+=1