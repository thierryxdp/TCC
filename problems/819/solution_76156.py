def filtraMultiplos(lista,n):
    i = 0 
    listanova = []
    while i < len(lista):
        if lista[i] % n == 0:
            listanova.append(lista[i])
        i = i + 1 
    return listanova