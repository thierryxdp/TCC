def eh_quadrada(matriz):
    '''a função retorna True se a matriz for quadrada
    list-> bool'''
    lista_vazia=[]
    if len(matriz)==len(matriz[0]):
        return True
    if matriz== lista_vazia:
        return True
    else:
        return False