def maiores(lista, n):
    """Retorna todos os números de uma lista maiores que n.
    Entrada: list, float
    Saída: list
    """
    list.append(lista, n)
    list.sort(lista)
    o = list.index(lista, n)+1
    return lista[o:]