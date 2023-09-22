def filtraMultiplos(lista, n):
    """
    funçao que dada uma lista, filtra os multiplos de um numero
    e retorna outra lista contendo todos os elementos da lista
    original que forem divisíveis pelo numero.
    :param lista: list 
    :param n: int
    :return: list
    """
    i = 0
    novaLista = []
    while i < len(lista):
        if lista[i] % n == 0:
            novaLista.append(lista[i])

        i += 1

    return novaLista