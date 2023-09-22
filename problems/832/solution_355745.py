def eh_quadrada(matriz):
    '''Retorna True se a matriz for quadrada e False caso não seja
    list -> bool'''
    if len(matriz) == len(matriz[0]) or len(matriz)==0:
        return True
    else: return False