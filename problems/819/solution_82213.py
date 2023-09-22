def filtraMultiplos(L,n):
    indice=0
    novo=()
    while indice<len(L):
        if L[indice]%n==0:
            novo=novo+L[indice]
        indice=indice+1
    return novo