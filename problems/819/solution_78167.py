def filtraMultiplos(lista, numero):
    i = 0
    listaco = []
    while i < len(lista):
        if lista[i] % numero == 0:
             lista[i] = listaco
        i = i + 1
    return listaco