def filtraMultiplos(lista, n):
    i = 0
    while i <= len(lista):
        if lista[i]%2 != 0:
            list.remove(lista, lista[i])
        i+=1
        return lista