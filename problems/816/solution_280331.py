def maiores(numeros: List[int], n: int):
    '''Funcao que calcula e retorna os numeros maiores que n.
    int->int'''
    from typing import List
    for i in numeros:
        if i > n:
            lista_final.append(i)
            return list(i)