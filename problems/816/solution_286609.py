def maiores(ls,n):
    """Recebe uma lista de números inteiros e um inteiro 'n'. Retorna
    outra lista com os números da lista de entrada que são maiores que
    'n', em ordem crescente.
    assinatura: list, int --> lits
    testes:
    maiores([22,2],11) == [22]
    maiores([10,12,14],16) == []
    """
    list.append(ls,n)
    list.sort(ls)
    return ls[list.index(ls,n) + 1:]