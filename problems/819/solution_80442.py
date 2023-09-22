def filtraMultiplos(lista,n):
    i = 0
    listaF = []

    while i<len(lista):
        if lista[i]%n==0:
            listaF+=[lista[i]]
        i+=1
    return listaF