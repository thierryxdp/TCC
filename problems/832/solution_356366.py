def eh_quadrada(matriz):
    """Recebe uma matriz e diz se a mesma eh quadrada,
       possuindo mesma quantidade de linha e coluna,
       retornando True para Quadrada, e False para
       Não Quadrada.

       list, -> bool"""
    
    quadrada = False
    for i in range(len(matriz)):
        if len(matriz[i]) == len(matriz):
            quadrada = True
        else:
            quadrada = False

    if matriz == []:
        return True
    return quadrada