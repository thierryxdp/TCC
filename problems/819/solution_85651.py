def filtraMultiplos(lista, n):
    '''Filtra os múltiplos de n em uma determinada lista de númuros'''
    i = 0
    novaLista = []
    while i < len(lista):
        if lista[i] % n == 0:
            novaLista.append(lista[i])

        i += 1

    return novaLista