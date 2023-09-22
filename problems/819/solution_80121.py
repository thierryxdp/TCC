def filtraMultiplos(listo, n):
    lista=list(listo)
    lista1=()
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            lista1.append(lista[i])
        i=i+1
    return tuple(lista1)