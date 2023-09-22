def eh_quadrada(matriz):
    '''recebe uma matriz e retorna True se ela for quadrada e False se não for.
    list(list) -> bool'''
    if len(matriz) ==  0:
        return True
    elif len(matriz) == len(matriz[0]) or len(matriz) == 0:
        return True
    else:
        return False