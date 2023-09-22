def eh_quadrada(matriz):
    '''funcao que identifica se a matriz dada como entrada é quadrada ou nao
    matriz->bool'''
    if matriz==[[]]:
        return ' '
    if len(matriz)==len(matriz[0]) :
        return True
    else:
        return False