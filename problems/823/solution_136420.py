def faltante(Lista):
    """A entrada é uma lista, que está no parâmetro, com N
    números inteiros - não repetidos - de 1 a N, porém uma das peças faltará
    e a saída é dizer qual a peça que falta"""
    #list -> int
    ListaN = Lista[:]
    list.sort(ListaN)
    n = ListaN[0]
    x = ListaN[-1] + 1
    indice = 0
    if 1 not in Lista:
        return 1
    elif ListaN == list(range(n, x)):
        return x
    while ListaN[indice] == list(range(n, x)):
        indice = indice + 1
    return indice +1