def eh_quadrada (matriz):
    ''' fala se a matriz e quadrada ou não;
    entrada:lista
    saida:bool'''
    if matriz==[]:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False