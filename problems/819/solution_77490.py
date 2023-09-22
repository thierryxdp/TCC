def filtraMultiplos(lista, n):
    i=0
    lista2=()

    while i<len(lista):
        if lista[i]%n==0:
            lista2[i]=lista[1]
        i=i+1

    return lista2