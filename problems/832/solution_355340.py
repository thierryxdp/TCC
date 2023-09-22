def eh_quadrada(matriz):
    ''' Função que verifica se uma matriz é ou não quadrada''' 
    if matriz==[[]]:
        return True
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False