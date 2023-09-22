def eh_quadrada(matriz):
    ''' Função que verifica se uma matriz é ou não quadrada''' 
    if len(matriz)== len(matriz[0]):
        return True
    elif matriz== [[]] :
        return True
    else:
        return False