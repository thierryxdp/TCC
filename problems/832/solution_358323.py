def eh_quadrada(matriz):
    '''funcao confirma se a matriz é quadrada ou não. list->bool'''
    if matriz==[]:
            return True
    for i in range(len(matriz)):
        if len(matriz)==(len(matriz[i])):
            return True
        else:
            return False