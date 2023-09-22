def eh_quadrada(matriz):
    '''Função que dada uma matriz, verifica se ela é quadrada ou não
    list -> bool'''
    if matriz == []:
        return True
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha == coluna:
        return True
    else:
        return False