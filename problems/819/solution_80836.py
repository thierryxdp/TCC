def filtraMultiplos(listaN, n):
    """
    Filtra os múltiplos de um número contido em uma lista e adiciona estes números em uma nova lista.
   list, int-> list
    """
    i = 0
    novLista = []
    
    while i < len(listaN):
        if lista[i] % n == 0:
            novaLista.append(lista[i])

    return novLista