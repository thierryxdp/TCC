def filtraMultiplos(lista, num):
    '''funcao que filtra os multiplos de uma lista e os
    	adiciona em uma nova lista
        lista-> list
        num-> int
        return: list
    '''
	n = 0
    novaLista = []
    while n < len(lista):
        if lista[n] % num == 0:
            novaLista.append(lista[n])

        n += 1

    return novaLista