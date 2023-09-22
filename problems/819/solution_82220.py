def filtraMultiplos(L,n):
    indice=0
    novo=[]
    while indice<len(L):
        Numero=L[indice]
        if Numero%n==0:
            novo=novo+numero
        indice=indice+1
    return novo