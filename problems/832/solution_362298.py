def eh_quadrada(matriz=[]):
    '''retorna se a matriz é ou nao quadrada'''
    '''list[lista] -> bool'''
    
    if len(matriz) == 0:
        return (True)
    linha = len(matriz)
    coluna = len(matriz[0])
    if liha == coluna:
        return (True)
    else:
        return (False)