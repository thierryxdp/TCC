def eh_quadrada(matriz):
    '''dada uma matriz, essa funcao identifica se ele eh quadrada
    list-->bool'''
    if (len(matriz)==len(matriz[0])) or (len(matriz)==0):
        return True
    else:
        return False