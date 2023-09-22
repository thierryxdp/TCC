def eh_quadrada(matriz):
    '''identificar se é uma matriz quadrada
    :return:bool->bool
    '''
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if len(matriz)== len(matriz[lin]) and len(matriz[col]):
                 return True
            
            else:
                 return False
            
            
            return True