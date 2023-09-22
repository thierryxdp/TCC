def filtraMultiplos(lista,n):
    i=0
    novo=[ ]
    while i<len(lista):
        if lista[i]%n==0:
            novo=novo+lista[i]
        i+=1
    return novo