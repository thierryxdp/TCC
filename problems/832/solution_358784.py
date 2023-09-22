def eh_quadrada(matriz):
    """Funcao calcula e retorna a identificao ,do elememto de entrada, e uma matriz 
    quadrada ou nao;
    list->bool"""
    if matriz==[]:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False