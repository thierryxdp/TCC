def eh_quadrada(matriz):
    """essa função recebe uma matriz qualquer e 
    define se ela é ou não uma matriz quadrada;
    list->bool"""
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True 
    else:
        return False