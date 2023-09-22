def maiores(l, n):
    """list, int -> list;
    Função que, dada uma lista de números inteiros e um nº
    inteiro n, retorna outra lista, com os números maiores
    que n ordenados em ordem crescente."""
    l.append(n)
    l.sort()
    l = l[n:]
    l.remove(n)
    return l