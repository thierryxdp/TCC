def eh_quadrada (matriz):
    ''' fala se a matriz e quadrada ou não;
    entrada:lista
    saida:bool'''
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False
    if matriz==[]:
        return True