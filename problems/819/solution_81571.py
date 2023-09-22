def filtraMultiplos(lista, n):
    i = 0
    novaLista = []
    while i < len(lista):
        if (lista[i] % n) == 0:
            novaLista[i] = lista[i]
        i=i+1
    return novaLista