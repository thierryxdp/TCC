def eh_quadrada(matriz):
    '''função que retorna True se a matriz quadrada e False
    caso não seja
    list(list)->bool'''
    if len(matriz)==len(matriz[0]):
        return True
    elif matriz==[]:
        return True
    else:
        return False