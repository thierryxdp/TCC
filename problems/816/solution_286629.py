def maiores(ls,n):
    """Recebe uma lista de números inteiros e um inteiro /n/. Retorna
    outra lista com os números da lista de entrada que são maiores que
    /n/, em ordem crescente.
    assinatura: list, int --> lits
    testes:
    maiores([0,1,2,3],5) == []
    maiores([0,2,3,5],1) == [2, 3, 5]
    """
    list.append(ls,n)
    list.sort(ls)
    return ls[list.index(ls,n) + 1:]