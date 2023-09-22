def eh_quadrada(matriz):
    '''a função retorna True se a matriz for quadrada
    list-> bool'''
    if len(matriz)==len(matriz[0]):
        return True
    if not matriz:
        return True
    else:
        return False