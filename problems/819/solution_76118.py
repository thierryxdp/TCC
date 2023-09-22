def filtraMultiplos(lista,n):
    pares=[]
    indice=1
    while indice < len(lista):
        if lista[indice]%n==0:
            pares=pares+[lista[indice],]
            indice=indice+1
    return pares