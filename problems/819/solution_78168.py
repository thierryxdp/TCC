def filtraMultiplos(lista, numero):
    i = 0
    listaco = []
    while i < len(lista):
        if lista[i] % numero == 0:
             lista[i] = lista + i
        i = i + 1
    return lista