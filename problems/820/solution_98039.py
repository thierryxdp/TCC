def posLetra(F,L,N):
    
    N = N - 1
    LZ = str.upper(L)
    
    X = str.replace(F,L,LZ,N)
    return X.find(L)