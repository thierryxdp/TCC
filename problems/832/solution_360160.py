def eh_quadrada(matriz):
    '''função que dada uma matriz retorna se ela é quadrada ou não:matriz->bool'''
    linha = len(matriz[0])
    coluna = len(matriz[0])
    if linha%coluna == 0:
        return True
    else:
        return False