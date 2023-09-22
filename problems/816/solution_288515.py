def maiores(l, n):
    """list, int -> list;
    Função que, dada uma lista de números inteiros e um nº
    inteiro n, retorna outra lista, com os números maiores
    que n ordenados em ordem crescente."""
    ret = l.copy()
    if not n in ret:
        ret.append(n)
    ret.sort()
    ret = ret[ret.index(n):]
    ret.remove(n)
    return ret