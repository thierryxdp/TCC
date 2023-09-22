def filtraMultiplos(lista, n):
    i=0
    lista2=(0, 0)

    while i<len(lista):
        if lista[i]%n==0:
            lista2[i]=lista[i]
        i=i+1

    return lista2