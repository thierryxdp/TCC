def fantante(L):
    X = list(range(len(L)))
    i=0
    faltante =[]
    
    while i < len(X):
        if X[i] not in L:
        	list.append(faltante,X[i])
        i=i+1
        
    return faltante