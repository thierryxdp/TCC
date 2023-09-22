def filtraMultiplos(lista, n):
    i = 0
    lista1 = list()
    while i < len(lista):
        mtp = lista[1]%n
        if mtp==0:
            list.append(lista1, lista[1])
        i=i+1
    return lista1