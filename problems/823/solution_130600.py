def faltante(L):
    i=0
    completo=list(range(1,len(L)+1))
    while i < len(L):
        if completo[i] not in L:
            return completo[i]
        i+=1
    return 0