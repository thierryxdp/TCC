def maiores(lista, n):
    """Dada uma lista e um numero, ele verifica o numero e traz a lista ordenada maior que n"""
    """list, int -> list"""
    lista.append(n)
    lista.sort()
    posicao = lista.index(n)
    return lista[posicao+1:]