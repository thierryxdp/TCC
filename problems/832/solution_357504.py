def eh_quadrada(matriz):
    '''funçao que dada uma matriz retorna se ela é quadrada ou nao'''
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    if nlinhas == ncolunas:
        return True
    else:
        return False