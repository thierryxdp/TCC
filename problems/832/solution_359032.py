def eh_quadrada(matriz):
    '''Funcao que indentifica se uma matriz e quadrada.
    lista->bool'''
    x=matriz[0]
    if len(x)==len(matriz) or len(x)==0:
        return True
    else:
        return False