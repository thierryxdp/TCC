def maiores(l, n):
    """list, int -> list;
    Função que, dada uma lista de números inteiros e um nº
    inteiro n, retorna outra lista, com os números maiores
    que n ordenados em ordem crescente."""
    ret = []
    #if l[i] > n:
    #    list.append(ret, l[i])
    for e in l:
        if e > n:
            list.append(ret, l[e])
    list.sort(ret)
    return ret