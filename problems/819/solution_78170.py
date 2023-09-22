def filtraMultiplos(lista, numero):
    i = 0
    listaNova = []
    while i < len(lista):
        if lista[i] % numero == 0:
             listaNova = lista + [lista[i],]
        i = i + 1
    return listaNova