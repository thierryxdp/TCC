def maiores(lis, n):
    """A função recebe uma lista e um valor, retornando uma segunda lista com todos os valores maiores do que n organizados em ordem crescente.
    assinatura: list(int) int -> list(int)"""
    maiores_numeros = list()
    for c in lis:
        if c > n:
            maiores_numeros.append(c)
            maiores_numeros.sort()
    return maiores_numeros