def filtraMultiplos(lista, n):
    '''ao receber uma lista de números inteiros e um número
    n inteiro, retorna a lista contendo apenas os números
    que são divisíveis por n.
    list, int -> list''''
    listaFinal = []
    prox = 0
    while prox < len(lista):
        if lista[prox] % n == 0:
            list.append(listaFinal, lista[prox])
        prox = prox + 1
    return listaFinal