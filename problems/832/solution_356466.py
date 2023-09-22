def eh_quadrada(matriz):
    """Função que identifica se uma matriz é quadrada. 
    matriz(lista de listas)-> bool"""
    if len(matriz) == len(matriz[0]):
        return True
    elif len(matriz) == 0:
        return True
    else:
        return False