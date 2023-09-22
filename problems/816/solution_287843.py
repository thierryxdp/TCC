def maiores(l, n):
    """Retorna uma lista apenas com os números maiores que n, da lista de entrada, em ordem crescente.
    list, int -> list"""
    l.append(n)
    l.sort()
    return l[l.index(n) + 1:]