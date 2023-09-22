def filtra_pares(elem):
    """Função recebe uma tupla com quatro elementos inteiros, e retorna
    uma nova tupla contendo apenas os elementos pares da tupla original
    entrada: tupla[int, int, int, int)
    retorno: int"""
    if elem[0:3]% 2== 0:
        return elem[0:3]