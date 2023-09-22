def maiores(ls,n):
    """Recebe uma lista de números inteiros e um inteiro /n/. Retorna
    outra lista com os números da lista de entrada que são maiores que
    /n/, em ordem crescente.
    assinatura: list, int --> lits
    testes:
    maiores([1,2,3,4],6) == []
    maiores([1,3,4,5],2) == [3, 4, 5]
    """
    list.append(ls,n)
    list.sort(ls)
    return ls[list.index(ls,n) + 1:]