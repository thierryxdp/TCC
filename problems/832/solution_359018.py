def eh_quadrada(matriz):
    '''Funcao que indentifica se uma matriz e quadrada.
    lista->bool'''
    x=matriz[0]
    y=matriz[1]
    if len(x)==len(matriz):
        return True
    else:
        return False