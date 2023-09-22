def eh_quadrada(matriz):
    """ identifica se uma matriz eh quadrada, sendo uma
    matriz vazia tambem considerada quadrada
    list -> bool"""
    for indice in range(len(matriz)):
        if len(matriz[indice]) != len(matriz):
            return False
    return True