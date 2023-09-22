def filtraMultiplos(lista,n):
    f=0
    outralista=[]
    while f<len(lista):
        if lista[f]%n==0:
            outralista.append(lista[f])
        f=f+1
    return outralista