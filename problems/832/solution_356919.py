def eh_quadrada(matriz):
    """A funcao diz se a matriz de entrada é quadrada ou nao, se for quadrada o retorno sera True
    se nao sera False.list(matriz)->bool"""
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]) :
        return True
    else:
        return False