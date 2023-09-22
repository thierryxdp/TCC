def eh_quadrada(matriz):
    '''identifica se uma matriz é quadrada'''
    '''list(list) -> bool'''
    linha = len(matriz)
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if len(matriz) == len(matriz[lin]) and len(matriz[col]):
                return True
            else:
                return False
    return True