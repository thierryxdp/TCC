def eh_quadrada(matriz):
    '''verifica se uma matriz e quadrada, e que ela contem nenhuma linha e coluna
    :return: bool->bool
    '''
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if len(matriz) == len(matriz[lin]) and len(matriz[col]):
                return True
            
            else:
                return False
    return True