def eh_quadrada(matriz):
    '''retorna True se a matriz de entrada for quadrada
    e false caso nao
    list->bool'''
    if len(matriz)==0:
        return True
    else:
        for i in range(len(matriz)):
            if len(matriz[i])!=len(matriz):
                return False
        return True