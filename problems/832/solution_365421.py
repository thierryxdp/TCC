def eh_quadrada(matriz):
    '''funcao booleana que identifica se uma matriz é quadrada'''
    if len(matriz)>0 and len(matriz)==len(matriz[0]):
        return True
    elif matriz==[]:
        return True
    else:
        return False