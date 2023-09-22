def filtraMultiplos(lista,n):
    L=[]
    indece=0
    while lista[indece]>n:
        lista[indece]% n!=0
        list.append(L,lista[indece])
        indece=indece+1
    return L