def maiores(l0, n):
    """Função recebe uma lista com números inteiros e um valor 'n' e retorna uma lista
    com todos os valores maiores que n em ordem crescente.
    list, int -> list"""
    l0.sort()
    l0.reverse()
    l1 = l0[0:n+1]
    l1.sort()
    return l1