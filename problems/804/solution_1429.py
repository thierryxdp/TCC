def filtra_pares(elem):
    """Função recebe uma tupla com quatro elementos inteiros, e retorna
    uma nova tupla contendo apenas os elementos pares da tupla original
    entrada: tupla(int, int, int, int)
    retorno: tupla(int)"""
    pares = tuple(x for x in elem if x% 2== 0)
    return pares