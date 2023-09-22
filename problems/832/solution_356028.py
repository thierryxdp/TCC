def eh_quadrada(matriz):
    '''verifica se uma matriz é quadrada
    list(list)->boolean'''
    if len(matriz)==0:
        return True
    if len(matriz)==len(matriz[0]):
        return True
    if len(matriz)>=1:
        return False