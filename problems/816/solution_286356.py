def maiores(ls, n):
    """Dada uma lista de números inteiros e um número
inteiro <n>, retorna uma lista com os elementos da lista
original que sejam maiores que <n> em ordem crescente.
assinatura: list, int --> list
casos de teste:
maiores([1,17, 2, 19], 4) == [17, 19]
maiores([1, 17, 17, 2, 19], 4) == [17, 17, 19]
maiores([2, 3, 4], 1) == [2, 3, 4]
maiores([2, 3, 4], 5) == []
"""
    list.append(ls, n)
    list.sort(ls)
    list.reverse(ls)
    indice_de_n = list.index(ls, n)
    ls2 = ls[ :indice_de_n]
    list.sort(ls2)
    return ls2