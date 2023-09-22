def filtraMultiplos(lista, numero):
    """retorna os múltiplos de um número contido em uma lista e adiciona estes números em uma nova lista.
    list,int-> list"""
    i = 0
    novaLista = []
    while i < len(lista):
        if lista[i] % numero == 0:
            novaLista.append(lista[i])

        i += 1
    return novaLista