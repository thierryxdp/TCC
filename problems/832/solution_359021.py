def eh_quadrada(matriz):
    '''Funcao que indentifica se uma matriz e quadrada.
    lista->bool'''
    x=matriz[0]
    if len(x)==len(matriz):
        return True
    if len(matriz)==0:
        return True
    else:
        return False