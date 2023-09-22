def maiores(ls,n):
    """Função que dado uma lista de números inteiros e um número inteiro qualquer (n), retorna ouutra lista, em ordem crescente,
de todos os valores maiores que "n".
list, int -> list
testes:
maiores([10,23,1,9,4],6) == [9, 10, 23]
[6, 9, 10, 23] == [5, 6]
"""
    list.append(ls,n)
    list.sort(ls)
    return ls[list.index(ls,n) + 1:]