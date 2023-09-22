def filtraMultiplos(lista, n):
    """
    função que recebe uma lista de números e um número, e retorna outra lista 
    contendo todos os elementos da lista original divisíveis por n
    :param lista: list 
    :param n: int
    :return: list
    """
    i = 0
    newlist = []
    while i < len(lista):
        if lista[i] % n == 0:
            newlist.append(lista[i])

        i += 1

    return newlist