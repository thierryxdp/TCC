def eh_quadrada(matriz):
    '''função que dada uma matriz retorna se ela é quadrada ou não:matriz->bool'''
    linha = len(matriz)
    elementos = len(matriz[0])
    coluna = (elementos/linha)
    while linha != coluna:
        return False
    if len(matriz) == len(matriz[0]):
        return True
    if matriz == []:
        return True