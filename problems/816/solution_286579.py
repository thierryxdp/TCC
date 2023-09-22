def maiores(ls,n):
    """Função que dada uma lista de números inteiros e um número inteiro qualquer (n), retorna outra lista, em ordem crescente e de todos os valores maiores que "n".
assinatura: list, int -> list
testes:
maiores([1,2,3,4],6) == []
maiores([11,30,42,50,120],87) == [120]
"""
    list.append(ls,n)
    list.sort(ls)
    return ls[list.index(ls,n) + 1:]