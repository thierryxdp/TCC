def filtraMultiplos(L,N):
    lista=[]
    for f in range(len(L)):
        if L[f]%N==0:
            lista.append(L[f])
    return lista