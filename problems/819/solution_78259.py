def filtraMultiplos(lista: list, n: int)-> list:
    """Dados uma lista e um número n, a função filtra os múltiplos
    de n desta lista, e retorna outra lista contendo todos os elementos
    da lista original que forem divisíveis por n"""
    lista1 = list()
    i = 0
    while (i < len(lista)):
        if (lista[i] % n == 0):
            list.append(lista1, lista[i])
        i += 1
    return lista1