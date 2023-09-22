def filtra_pares(elem):
    """Função recebe uma tupla com quatro elementos inteiros, e retorna
    uma nova tupla contendo apenas os elementos pares da tupla original
    entrada: tupla(int, int, int, int)
    retorno: tupla(int)"""
    if elem[0]% 2== 0:
        x = elem[0]
    if elem[1]% 2== 0:
        x1 = x,elem[1]
    if elem[2]% 2== 0:
        x2 = x1,elem[2]
    if elem[3]% 2== 0:
        x3 = x2,elem[3]
    return x+ x1+ x2+ x3