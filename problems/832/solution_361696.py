def eh_quadrada(matriz):
    '''identifica se uma matriz é quadrada'''
    '''list(list) -> bool'''
    linha = len(matriz)
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            if len(matriz) == len(matriz[linha]) and len(matriz[coluna]):
                return True
            else:
                return False
    return True