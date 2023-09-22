def filtra_pares(t):
    """Função que recebe uma tupla com 4 elementos inteiros e retorna
    uma nova tupla contendo apenas os elementos pares da tupla original"""
   
    t = list(t)
    pares = []
    for i in t:
        if(i % 2 == 0):
            pares.append(i)
    return tuple(pares)