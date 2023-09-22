def filtraMultiplos(lista, n):
    i = 0
    lista1 = list()
    while i < len(lista):
        mtp = lista[i]%n
        if mtp==0:
            list.append(lista1, lista[i])
        i=i+1
    return lista1