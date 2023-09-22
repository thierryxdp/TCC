def filtra_pares(elem):
    """Função recebe uma tupla com quatro elementos inteiros, e retorna
    uma nova tupla contendo apenas os elementos pares da tupla original
    entrada: tupla[int, int, int, int)
    retorno: int"""
    if elem[0]% 2== 0:
        if elem[1]% 2== 0:
            if elem[2]% 2== 0:
                if elem[3]% 2== 0:
                    return elem[0:3]
                else:
                    return elem[0:2]
            elif elem[3]% 2== 0:
                    return elem[0:1], elem[3]
            else:
                    return elem[0:1]
        elif elem[2]% 2== 0:
            if elem[3]% 2== 0:
                return elem[0], elem[2:3]
            else:
               return elem[0], elem[2]
        elif elem[3]% 2== 0:
            return elem[0], elem[3]
        elif elem[1]% 2== 0:
            if elem[2]% 2== 0:
                if elem[3]% 2== 0:
                    return elem[1:3]
                else
                    return elem[1:2]