def filtra_pares(elem):
    """Função recebe uma tupla com quatro elementos inteiros, e retorna
    uma nova tupla contendo apenas os elementos pares da tupla original
    entrada: tupla(int, int, int, int)
    retorno: tupla(int)"""
    x = ()
    if elem[0]% 2== 0:
        x = elem[0]
    if elem[1]% 2== 0:
        if len(x) = 0:
            x = elem[1]
        else:
            x = x,elem[1]
    if elem[2]% 2== 0:
        if x = ():
            x = elem[2]
        else:
            x = x,elem[2]
    if elem[3]% 2== 0:
        if x = ():
            x = elem[3]
        else:
            x = x,elem[3]
    return x