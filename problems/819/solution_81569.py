def filtraMultiplos(lista, n):
    i = 0
    while i < len(lista):
        if (lista[i] % n) == 0:
            novaLista[i] = lista[i]
        i++
    return novaLista