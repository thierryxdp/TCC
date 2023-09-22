def faltante(L):
    X = list(range(1,len(L)+2))
    i=0
    faltante =[]
    while i < len(X):
        if X[i] not in L:
            list.append(faltante,X[i])
        i=i+1
        
    return faltante[0]