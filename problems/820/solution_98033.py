def posLetra(F,L,N):
    N = N - 1
    LZ = str.upper(L)
    
    str.replace(F,L,LZ,N)
    return str.index(F,L)