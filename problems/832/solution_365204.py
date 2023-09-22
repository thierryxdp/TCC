def eh_quadrada(matriz):
    '''dada uma matriz a funcao avalia e retorna se a 
    mesma e quadrada ou nao
    matriz --> bool'''
    linha = len(matriz)
    coluna = len(matriz[:])
    if matriz == []:
        return True
    elif linha == coluna:
        return True
    else:
        return False