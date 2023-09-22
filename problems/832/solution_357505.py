def eh_quadrada(matriz):
    '''funçao que dada uma matriz retorna se ela é quadrada ou nao'''
    nlinhas = len(matriz)
    if len(matriz) == 0:
        return True
    ncolunas = len(matriz[0])
    if nlinhas == ncolunas:
        return True
    else:
        return False